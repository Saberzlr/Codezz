<template>
    <div>
        <h1>员工管理</h1>
        <el-row>
            <el-col :span="4">
                <el-input v-model="query.ename" placeholder="请输入姓名搜索"></el-input>
            </el-col>
            <el-col :span="2">
                <el-button type="primary" @click="search">搜索</el-button>
            </el-col>

            <el-col :span="4">
                <el-button type="primary" @click="showAddDialog">添加员工</el-button>
            </el-col>
            
        </el-row>

        <el-table
            :data="empList"
            border
            style="width: 100%">
            <el-table-column
            prop="empno"
            label="编号"
            width="180">
            </el-table-column>
            <el-table-column
            prop="ename"
            label="姓名"
            width="180">
            </el-table-column>
            <el-table-column
            prop="job"
            label="职位">
            </el-table-column>
            <el-table-column
            prop="hiredate"
            label="入职日期">
            </el-table-column>
            <el-table-column
            prop="sal"
            label="工资">
            </el-table-column>
            <el-table-column
            prop="comm"
            label="津贴">
            </el-table-column>
            <el-table-column
            label="头像">
                <template slot-scope="scope">
                    <img :src="scope.row.pic" style="width: 50px;height: 50px;">
                </template>
            </el-table-column>
            <el-table-column label="操作">
                <template slot-scope="scope">
                    <el-button
                    size="mini"
                    @click="showEditDialog(scope.row)">编辑</el-button>
                    <el-button
                    size="mini"
                    type="danger"
                    @click="handleDelete(scope.row)">删除</el-button>
                </template>
            </el-table-column>
        </el-table>

        <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="query.currentPage"
            :page-sizes="[5, 8, 10]"
            :page-size="query.pageSize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="totalRows">
        </el-pagination>

        <!-- 添加员工信息 -->
        <el-dialog :title="dialogTitle" :visible.sync="dialogFormVisible">
            <el-form :model="form">
                <el-form-item label="员工姓名" :label-width="formLabelWidth">
                    <el-input v-model="form.ename" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="员工职位" :label-width="formLabelWidth">
                <el-select v-model="form.job" placeholder="请选择员工职位">
                    <el-option label="会计" value="会计"></el-option>
                    <el-option label="销售" value="销售"></el-option>
                    <el-option label="研发" value="研发"></el-option>
                    <el-option label="产品经理" value="产品经理"></el-option>
                    <el-option label="文员" value="文员"></el-option>
                </el-select>
                </el-form-item>
                <el-form-item label="入职日期" :label-width="formLabelWidth">
                    <el-date-picker
                            v-model="form.hiredate"
                            type="date"
                            placeholder="选择日期">
                    </el-date-picker>
                </el-form-item>
                <el-form-item label="员工工资" :label-width="formLabelWidth">
                    <el-input v-model.number="form.sal" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="员工津贴" :label-width="formLabelWidth">
                    <el-input v-model.number="form.comm" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="头像链接" :label-width="formLabelWidth">
                    <el-input v-model="form.pic" autocomplete="off"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">取 消</el-button>
                <el-button type="primary" @click="handleAddOrUpdate">{{submitText}}</el-button>
            </div>
            
        </el-dialog>

    </div>
</template>

<script>
import axios from "axios";
export default {
    name: 'EmpView',
    data() {
        return {
            query: {
                currentPage: 1,
                pageSize: 5,
                ename: ''
            },
            //分页查询的结果  总记录数
            totalRows: 0,
            //分页查询的结果  员工集合数据
            empList: [],
            //对话框是否显示
            dialogFormVisible: false,
            dialogTitle: '添加员工',
            submitText: '确认添加',
            //收集对话框上的表单数据
            form:{
                ename: '',
                job: '',
                hiredate: '',
                sal: 0,
                comm: 0,
                pic: ''
            },
            formLabelWidth: '120px'
        }
    },
    methods: {
        handleAddOrUpdate(){
            if(this.form.empno){
                // 修改
                this.handleUpdate();
            }else{
                // 添加
                this.handleAdd();
            }
        },
        showEditDialog(row){
            this.dialogTitle = '修改员工';
            this.submitText = '确认修改';
            //数据回显
            console.log(row);
            this.form = Object.assign({},row); //复制一个对象的属性给另一个对象
            this.dialogFormVisible = true;
        },
        handleDelete(row){
            this.$confirm('您确定要永久删除该员工信息吗?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                axios({
                    method: 'delete',
                    url: 'http://localhost:8080/emp/'+row.empno
                }).then(res=>{
                    if(res.data == 'success'){
                        this.$message({
                            type: 'success',
                            message: '删除成功!'
                        });
                        this.getData();
                    }else{
                        this.$message({
                            type: 'error',
                            message: '删除失败!'
                        });
                    }
                })

                
            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消删除'
                });          
            });
        },
        handleAdd(){
            console.log(this.form);
            axios({
                method: 'post',
                url: 'http://localhost:8080/emp',
                data: this.form
            }).then(res=>{
                console.log(res.data);
                if (res.data == 'success') {
                    this.dialogFormVisible = false;
                    this.$message.success('添加成功');
                    this.query.currentPage = 1;
                    this.getData();
                }else{
                    this.$message.error('添加失败，请重试');
                }
            })
        },
        handleUpdate(){
            console.log(this.form);
            axios({
                method: 'put',
                url: 'http://localhost:8080/emp',
                data: this.form
            }).then(res=>{
                console.log(res.data);
                if (res.data == 'success') {
                    this.dialogFormVisible = false;
                    this.$message.success('修改成功');
                    this.getData();
                }else{
                    this.$message.error('修改失败，请重试');
                }
            })
        },
        showAddDialog(){
            this.dialogTitle = '添加员工';
            this.submitText = '确认添加';
            this.form = {
                ename: '',
                job: '',
                hiredate: '',
                sal: 0,
                comm: 0,
                pic: ''
            };

            this.dialogFormVisible = true;
        },
        search(){
            this.query.currentPage = 1;
            this.getData();
        },
        handleSizeChange(val) {
            console.log(`每页 ${val} 条`);
            this.query.pageSize = val;
            this.getData();
        },
        handleCurrentChange(val) {
            console.log(`当前页: ${val}`);
            this.query.currentPage = val;
            this.getData();
        },
        getData(){
            axios({
                method: 'post',
                url: 'http://localhost:8080/emp/page',
                data: this.query
            }).then(res=>{
                console.log(res.data.totalPages);
                this.totalRows = res.data.totalRows;
                this.empList = res.data.data;
            })
        }
    },
    mounted() {
        this.getData();
    },
}
</script>

<style>

</style>
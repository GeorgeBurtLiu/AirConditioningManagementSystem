<template>
    <div class="container">
        <div class="col-lg-6 offset-lg-3">
            <div class="row">
                <b-input-group>
                    <b-form-input placeholder="请输入用户名" required autofocus></b-form-input>
                    <b-input-group-append>
                        <b-button variant="outline-warning">清除</b-button>
                    </b-input-group-append>
                </b-input-group>
            </div>
            <p></p>
            <div class="row">
                <b-input-group>
                    <b-form-input type="password" placeholder="请输入密码" required></b-form-input>
                    <b-input-group-append>
                        <b-button variant="outline-info">查看</b-button>
                    </b-input-group-append>
                </b-input-group>
            </div>
            <p></p>
            <div class="row">
                <b-checkbox class=" mb-3" value="remember-me">Remember me</b-checkbox>
            </div>
            <div class="row">
                <b-button variant="outline-primary" class="col-lg-2 offset-lg-5">登陆</b-button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Login"
    }
</script>

<style scoped>

</style>

<template>
    <div>
        <div class="modal-card">
            <div class="login_warp">
                <section>
                    <b-field label="Email">
                        <b-input type="email" placeholder="example@gmail.com" maxlength="50"></b-input>
                    </b-field>
                    <b-field label="Password">
                        <b-input type="password" placeholder="password input" password-reveal></b-input>
                    </b-field>
                </section>
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
    .modal-card {
        width: 600px;
        height: 600px;
        background: rgb(232, 232, 232);
    }
    .login_warp {
        padding: 10% 25%;
        width: 100%;
        height: 100%;
    }
    .level-item {
        width: 100%;
        height: 20%;
        border: 1px solid;
    }
</style>
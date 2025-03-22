<script setup>
import { ref } from 'vue';
import axios from 'axios';
import router from '../router';


const user_mail = ref("");
const password = ref("");



function login() {
    console.log("Login button has been clicked");
    if (!this.user_mail || !this.password) {
        alert("Please fill all the fields");
        return;
    }
    console.log(this.user_mail);

    axios.post("http://127.0.0.1:8081/api/login", {
        "email": this.user_mail,
        "password": this.password
    }).then((response) => {
        console.log(response)
        if (response.data.status == "success") {
            alert(response.data.message);
            const access_token = response.data.access_token;
            const user_name = response.data.user_name;
            const user_mail_1 = response.data.user_mail

            localStorage.setItem("access_token", access_token);
            localStorage.setItem("user_name", user_name);
            localStorage.setItem("user_mail", user_mail_1);

            router.push({ name: 'home' })



        }
        if (response.data.status == "failed") {
            alert(response.data.message);
            this.reset()
        }
    }).catch((error) => {
        console.error(error);
    })
};


function reset() {
    this.user_mail = "";
    this.password = "";
}
</script>

<template>
    <div>
        <h3>Login Page</h3>
        <form>
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email address</label>
                <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
                    v-model="user_mail">
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                <input type="password" class="form-control" id="exampleInputPassword1" v-model="password">
            </div>
            <button type="button" class="btn btn-primary" @click="login()">Submit</button> &nbsp; &nbsp;
            <button type="button" class="btn btn-danger" @click="reset()">Reset</button>

        </form>
    </div>
</template>
<style scoped></style>
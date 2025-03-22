<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';


const name = ref("");
const user_mail = ref("");
const password = ref("");
const re_password = ref("");
const role = ref("")
const allRole = ref([])

onMounted(() => {
    console.log(`the component is now mounted.`)
    getAllRoles();
})

function getAllRoles() {
    axios.get("http://127.0.0.1:8081/api/role").then((response) => {
        console.log(response.data)
        allRole.value = response.data
    }).catch((error) => {
        console.error(error);
    })
}

function register() {
    console.log("register button has been clicked");
    if (!this.name || !this.user_mail || !this.password || !this.re_password) {
        alert("Please fill all the fields");
        return;
    }
    if (!this.role) {
        alert("Please fill the role");
        return;
    }
    if (this.password != this.re_password) {
        alert("Password doesn't match");
        return;
    }

    axios.post("http://127.0.0.1:8081/api/register", {
        "email": this.user_mail,
        "password": this.password,
        "role": this.role,
        "name": this.name
    }).then((response) => {
        console.log(response)
        if (response.data.status == "success") {
            alert(response.data.message);
            this.reset();
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
    this.name = "";
    this.password = "";
    this.re_password = "";
    this.role = "";
    this.user_mail = "";
}
</script>

<template>
    <div>
        <h3>Register Page</h3>
        <form>
            <div class="mb-3">
                <label for="name" class="form-label">Name</label>
                <input type="text" class="form-control" id="name" v-model="name">
            </div>
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email address</label>
                <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
                    v-model="user_mail">
                <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                <input type="password" class="form-control" id="exampleInputPassword1" v-model="password">
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword2" class="form-label">Re-Password</label>
                <input type="password" class="form-control" id="exampleInputPassword2" v-model="re_password">
            </div>
            <div class="mb-3">
                <label for="role" class="form-label">Role</label>
                <select class="form-select" id="role" v-model="role">
                    <option v-for="role in allRole" :key="role.id" :value="role.name">{{ role.name }}</option>
                </select>
            </div>
            <button type="button" class="btn btn-primary" @click="register()">Submit</button> &nbsp; &nbsp;
            <button type="button" class="btn btn-danger" @click="reset()">Reset</button>

        </form>
    </div>
</template>
<style scoped></style>
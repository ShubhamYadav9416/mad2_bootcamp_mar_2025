<script setup>
import { onMounted } from 'vue';
import router from '../router';
import axios from 'axios';

onMounted(() => {
    check_page_access();
})

function check_page_access() {
    let access_token = localStorage.getItem('access_token')
    console.log(access_token)
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + access_token
    axios.get("http://127.0.0.1:8081/api/check_page_access").then((response) => {
        if (response.data.status == "success"){
            return;
        }
        else{
            router.push({ name: 'login' });
            alert("You don't have access to Home Page")
        }

    }).catch((error) => {
        console.error(error);
        router.push({ name: 'login' });
        alert("You don't have access to Home Page")
    })
}

</script>


<template>
    <div>
        <p>This is Home page</p>
    </div>
</template>
<style scoped></style>
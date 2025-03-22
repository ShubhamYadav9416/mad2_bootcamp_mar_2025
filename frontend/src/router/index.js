import { createWebHistory,createRouter } from "vue-router";

import HomeView from "@/view/HomeView.vue";
import ProfileView from "@/view/ProfileView.vue";
import NotFoundView from "@/view/NotFoundView.vue";
import LoginView from "@/view/LoginView.vue";
import RegisterView from "@/view/RegisterView.vue";

const routes = [
    {path: "/home", name: 'home', component: HomeView},
    {path: "/profile",name: 'profile', component: ProfileView},
    {path: "/login",name: 'login', component:LoginView},
    {path: "/register",name: 'register', component: RegisterView},
    {path: "/:pathMatch(.*)*", component: NotFoundView}
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;
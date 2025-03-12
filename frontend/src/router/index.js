import { createWebHistory,createRouter } from "vue-router";

import HomeView from "@/view/HomeView.vue";
import ProfileView from "@/view/ProfileView.vue";
import NotFoundView from "@/view/NotFoundView.vue";
import LoginView from "@/view/LoginView.vue";
import RegisterView from "@/view/RegisterView.vue";

const routes = [
    {path: "/home", component: HomeView},
    {path: "/profile", component: ProfileView},
    {path: "/login", component:LoginView},
    {path: "/register", component: RegisterView},
    {path: "/:pathMatch(.*)*", component: NotFoundView}
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;
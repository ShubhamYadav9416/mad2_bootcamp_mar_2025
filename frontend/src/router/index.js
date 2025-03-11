import { createWebHistory,createRouter } from "vue-router";

import HomeView from "@/view/HomeView.vue";
import ProfileView from "@/view/ProfileView.vue";

const routes = [
    {path: "/home", component: HomeView},
    {path: "/profile", component: ProfileView}
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;
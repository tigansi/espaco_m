import Vue from "vue";
import { IonicVueRouter } from "@ionic/vue";

Vue.use(IonicVueRouter);

/* Proteção da rota */
function guardaRota(to, from, next) {
  var isAuthenticated = false;
  if (localStorage.getItem("isLogado")) isAuthenticated = true;
  else isAuthenticated = false;
  if (isAuthenticated) {
    next();
  } else {
    next("/login");
  }
}

const routes = [
  {
    path: "/",
    redirect: "Login",
  },
  {
    path: "/Login",
    name: "Login",
    component: () => import("@/views/acesso/Login"),
  },
  {
    path: "/Cadastro",
    name: "Cadastro",
    component: () => import("@/views/acesso/Cadastro"),
  },
  {
    path: "/PainelClientes",
    name: "PainelClientes",
    beforeEnter: guardaRota,
    component: () => import("@/views/clientes/PainelClientes"),
  },
];

const router = new IonicVueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

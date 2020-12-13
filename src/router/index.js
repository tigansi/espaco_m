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
    path: "/EscolhaPapel",
    name: "EscolhaPapel",
    beforeEnter: guardaRota,
    component: () => import("@/views/acesso/EscolhaPapel"),
  },
  {
    path: "/HomePainelClientes",
    name: "HomePainelClientes",
    beforeEnter: guardaRota,
    component: () => import("@/views/clientes/HomePainelClientes"),
    children: [
      {
        path: "HomeClientes",
        name: "HomeClientes",
        beforeEnter: guardaRota,
        component: () => import("@/views/clientes/painel/HomeClientes"),
        children: [
          {
            path: "Agendar",
            name: "Agendar",
            beforeEnter: guardaRota,
            component: () => import("@/views/clientes/painel/tabs/Agendar"),
          },
          {
            path: "Profissionais",
            name: "Profissionais",
            beforeEnter: guardaRota,
            component: () =>
              import("@/views/clientes/painel/tabs/Profissionais"),
          },
          {
            path: "Servicos",
            name: "Servicos",
            beforeEnter: guardaRota,
            component: () => import("@/views/clientes/painel/tabs/Servicos"),
          },
        ],
      },
      {
        path: "MinhaAgenda",
        name: "MinhaAgenda",
        beforeEnter: guardaRota,
        component: () => import("@/views/clientes/painel/MinhaAgenda"),
      },
      {
        path: "PerfilCliente",
        name: "PerfilCliente",
        beforeEnter: guardaRota,
        component: () => import("@/views/clientes/painel/PerfilCliente"),
      },
    ],
  },
];

const router = new IonicVueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

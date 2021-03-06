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
  {
    path: "/HomePainelAdm",
    name: "HomePainelAdm",
    beforeEnter: guardaRota,
    component: () => import("@/views/administrador/HomePainelAdm"),
    children: [
      {
        path: "PainelPessoal",
        name: "PainelPessoal",
        beforeEnter: guardaRota,
        component: () => import("@/views/administrador/painel/PainelPessoal"),
        children: [
          {
            path: "CadastrarPessoas",
            name: "CadastrarPessoas",
            component: () =>
              import(
                "@/views/administrador/painel/tabsPessoal/CadastrarPessoas"
              ),
          },
          {
            path: "ListagemPessoas",
            name: "ListagemPessoas",
            component: () =>
              import(
                "@/views/administrador/painel/tabsPessoal/ListagemPessoas"
              ),
          },
        ],
      },
      {
        path: "PainelServicos",
        name: "PainelServicos",
        beforeEnter: guardaRota,
        component: () => import("@/views/administrador/painel/PainelServicos"),
        children: [
          {
            path: "CadastrarCategorias",
            name: "CadastrarCategorias",
            beforeEnter: guardaRota,
            component: () =>
              import(
                "@/views/administrador/painel/tabsServicos/CadastrarCategorias"
              ),
          },
          {
            path: "CadastrarServicos",
            name: "CadastrarServicos",
            beforeEnter: guardaRota,
            component: () =>
              import(
                "@/views/administrador/painel/tabsServicos/CadastrarServicos.vue"
              ),
          },
        ],
      },
      {
        path: "PainelRelatorios",
        name: "PainelRelatorios",
        beforeEnter: guardaRota,
        component: () =>
          import("@/views/administrador/painel/PainelRelatorios"),
      },
    ],
  },
  {
    path: "/HomePainelColaborador",
    name: "HomePainelColaborador",
    beforeEnter: guardaRota,
    component: () => import("@/views/colaborador/HomePainelColaborador"),
    children: [
      {
        path: "HomeAgenda",
        name: "HomeAgenda",
        beforeEnter: guardaRota,
        component: () => import("@/views/colaborador/painel/HomeAgenda"),
        children: [
          {
            path: "Agenda",
            name: "Agenda",
            beforeEnter: guardaRota,
            component: () =>
              import("@/views/colaborador/painel/tabsAgenda/Agenda"),
          },
          {
            path: "ConfigAgenda",
            name: "ConfigAgenda",
            beforeEnter: guardaRota,
            component: () =>
              import("@/views/colaborador/painel/tabsAgenda/ConfigAgenda"),
          },
        ],
      },
      {
        path: "PerfilColaborador",
        name: "PerfilColaborador",
        beforeEnter: guardaRota,
        component: () => import("@/views/colaborador/painel/PerfilColaborador"),
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

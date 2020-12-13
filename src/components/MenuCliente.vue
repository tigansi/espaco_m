<template>
  <ion-menu content-id="main" side="start" type="push" id="main-menu">
    <ion-header>
      <ion-toolbar>
        <ion-title>Espaço M</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content>
      <ion-list>
        <ion-menu-toggle auto-hide="false">
          <ion-item
            button
            @click="$router.push('/HomePainelClientes/HomeClientes/Agendar')"
          >
            <ion-icon slot="start" name="home"></ion-icon>
            <ion-label>
              <span>Início</span>
            </ion-label>
          </ion-item>
          <ion-item
            button
            @click="$router.push('/HomePainelClientes/PerfilCliente')"
          >
            <ion-icon slot="start" name="person"></ion-icon>
            <ion-label>
              <span>Perfil do cliente</span>
            </ion-label>
          </ion-item>
          <ion-item
            button
            @click="
              $router.push('/HomePainelClientes/MinhaAgenda')
            "
          >
            <ion-icon slot="start" name="calendar"></ion-icon>
            <ion-label>
              <span>Minha agenda</span>
            </ion-label>
          </ion-item>
          <ion-item button @click="logOut()">
            <ion-icon slot="start" name="exit"></ion-icon>
            <ion-label>
              <span>Sair</span>
            </ion-label>
          </ion-item>
        </ion-menu-toggle>
      </ion-list>
    </ion-content>
    <ion-footer>
      <center>
        <!-- Image e nome do pessoa -->
      </center>
    </ion-footer>
  </ion-menu>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {
    logOut() {
      localStorage.clear();
      this.$router.push("/Login");
    },
  },
  mounted() {
    //var dados = JSON.parse(localStorage.getItem("isLogado"));
  },
};
</script>

<style></style>

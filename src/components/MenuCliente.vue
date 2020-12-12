<template>
  <ion-menu content-id="main" side="start" type="push" id="main-menu">
    <ion-header>
      <ion-toolbar>
        <ion-title>Espaço M</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content>
      <ion-list>
        <ion-item></ion-item>
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

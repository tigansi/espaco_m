<template>
  <ion-page>
    <ion-header>
      <ion-toolbar id="page" style="color:white">
        <ion-title>{{ nome }}</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content id="page" class="ion-padding">
      <ion-grid>
        <center>
          <ion-row>
            <ion-col size-md="4" class="ion-hide-xl-down"> </ion-col>
            <ion-col size-sm="12" size-md="4">
              <div class="box">
                <ion-icon size="large" name="cut"></ion-icon><br />
                Acessar como funcionário
              </div>
              <br />
              <div class="box">
                <ion-icon size="large" name="bag"></ion-icon><br />
                Acessar como cliente
              </div>
              <br />
              <div class="box" v-if="tipo == 'ADM'">
                <ion-icon size="large" name="laptop"></ion-icon><br />
                Acessar como administrador
              </div>
              <br />
              <div class="box" @click="logOut">
                <ion-icon size="large" name="exit"></ion-icon><br />
                Voltar para o login
              </div>
            </ion-col>
            <ion-col size-md="4" class="ion-hide-xl-down"> </ion-col>
          </ion-row>
        </center>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script>
import { addIcons } from "ionicons";
import { cut, bag, laptop, exit } from "ionicons/icons";

addIcons({
  "md-cut": cut,
  "ios-cut": cut,
  "md-bag": bag,
  "ios-bag": bag,
  "ios-laptop": laptop,
  "md-laptop": laptop,
  "md-exit": exit,
  "ios-exit": exit,
});
export default {
  data() {
    return {
      nome: "",
      tipo: "",
    };
  },
  methods: {
    logOut() {
      localStorage.clear();
      this.$router.push("/Login");
    },
  },
  mounted() {
    var dados = JSON.parse(localStorage.getItem("isLogado"));
    this.nome = dados.nm_usuario;
    this.tipo = dados.tipo;
  },
};
</script>

<style>
#page {
  --background: rgb(55, 52, 53);
}

.box {
  transition: box-shadow 0.3s;
  /*width: 120px;
  height: 90px;*/
  /*margin: 50px;*/
  border-radius: 10px;
  border: 1px solid #ccc;
  background: #fff;
  /*float: left;*/
  padding: 8px;
  text-align: center;
  color: rgb(133, 100, 4);
  cursor: pointer;
}
.box:hover {
  box-shadow: 0 0 11px rgba(33, 33, 33, 0.2);
}
</style>

<template>
  <ion-page>
    <ion-content id="page">
      <ion-card style="background-color:white;">
        <ion-card-header>
          <ion-grid>
            <ion-row>
              <ion-col size-md="9" size-sm>
                <ion-card-subtitle>Bem vindo(a)</ion-card-subtitle>
                <ion-card-title>{{ nome }} </ion-card-title>
              </ion-col>
              <ion-col>
                <center>
                  <ion-avatar>
                    <ion-img
                      :src="'http://192.168.8.7:5000/fotos?caminho=' + foto"
                    ></ion-img>
                  </ion-avatar>
                </center>
              </ion-col>
            </ion-row>
          </ion-grid>
        </ion-card-header>
        <ion-card-content>
          
        </ion-card-content>
      </ion-card>
    </ion-content>
  </ion-page>
</template>

<script>
export default {
  data() {
    return {
      nome: "",
      foto: "",
    };
  },
  methods: {
    inicializa() {
      var dados = JSON.parse(localStorage.getItem("isLogado"));
      this.nome = dados.nm_usuario;
      this.foto = dados.foto;
    },
  },
  mounted() {
    this.inicializa();
  },
};
</script>

<style>
#page {
  --background: rgb(55, 52, 53);
}
</style>

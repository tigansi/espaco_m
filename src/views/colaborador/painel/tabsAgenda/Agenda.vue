<template>
  <ion-page>
    <ion-content id="page">
      <ion-grid>
        <ion-row>
          <ion-col size="12">
            <ion-card style="background-color:white">
              <ion-card-header>
                <ion-grid>
                  <ion-row>
                    <ion-col size-md="9" size-sm="9">
                      <ion-card-subtitle>Bem vindo(a)</ion-card-subtitle>
                      <ion-card-title>{{ nome_col }} </ion-card-title>
                    </ion-col>
                    <ion-col>
                      <center>
                        <ion-avatar slot="end">
                          <ion-img
                            :src="
                              'http://192.168.8.7:5000/fotos?caminho=' + foto
                            "
                          ></ion-img>
                        </ion-avatar>
                      </center>
                    </ion-col>
                  </ion-row>
                </ion-grid>
              </ion-card-header>
            </ion-card>
            <ion-card style="background-color:white">
              <ion-card-content>
                <ion-list>
                  <ion-list-header>
                    <h1>Agenda do dia</h1>
                  </ion-list-header>
                  <div>
                    <ion-item></ion-item>
                  </div>
                </ion-list>
              </ion-card-content>
            </ion-card>

            <ion-card style="background-color:white">
              <ion-card-content>
                <ion-list>
                  <ion-list-header>
                    <h1>Agenda geral</h1>
                  </ion-list-header>
                </ion-list>
              </ion-card-content>
            </ion-card>
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script>
export default {
  data() {
    return {
      nome_col: "",
      foto: "",
      id_usuario: "",
    };
  },
  methods: {},
  mounted() {
    var dados = JSON.parse(localStorage.getItem("isLogado"));
    this.nome_col = dados.nm_usuario;
    this.foto = dados.foto;
    this.id_usuario = dados.id_usuario;
  },
};
</script>

<style>
#page {
  --background: rgb(55, 52, 53);
}
</style>

<template>
  <ion-page>
    <ion-content id="page">
      <ion-refresher mode="md" slot="fixed" @ionRefresh="doRefresh($event)">
        <ion-refresher-content
          pulling-icon="chevron-down-circle-outline"
          refreshing-text="Atualizando..."
        ></ion-refresher-content>
      </ion-refresher>
      <ion-grid>
        <ion-row>
          <ion-col size="12">
            <ion-card style="background-color: white">
              <ion-card-content>
                <ion-list>
                  <ion-item>
                    <ion-avatar slot="start">
                      <ion-img
                        :src="'http://192.168.8.7:5000/fotos?caminho=' + foto"
                      ></ion-img>
                    </ion-avatar>
                    <ion-label>
                      <h2>Bem vindo(a)</h2>
                      <p>{{ nome_adm }}</p>
                    </ion-label>
                  </ion-item>
                </ion-list>
              </ion-card-content>
            </ion-card>
          </ion-col>
          <ion-col size-md="6" size-sm="12">
            <ion-card style="background-color: white">
              <ion-card-content>
                <ion-list>
                  <ion-list-header>
                    <h1>Categorias</h1>
                  </ion-list-header>
                  <div id="form">
                    <ion-item>
                      <ion-label position="floating"
                        >Nome da categoria</ion-label
                      >
                      <IonInputVue v-model="nome_cat" />
                    </ion-item>
                  </div>
                </ion-list>
                <ion-button @click="efetuaCadastro" size="block" id="btn_cad"
                  >Cadastrar</ion-button
                >
              </ion-card-content>
            </ion-card>
          </ion-col>
          <ion-col size-md="6" size-sm="12">
            <ion-card style="background-color: white">
              <ion-card-content>
                <ion-list>
                  <ion-list-header>
                    <h1>Listagem</h1>
                  </ion-list-header>
                  <div v-for="cat of categorias" :key="cat.id_categoria">
                    <ion-item>
                      <ion-grid>
                        <ion-row>
                          <ion-col size-md="10" size="9" size-sm>{{
                            cat.nm_categoria
                          }}</ion-col>
                          <ion-col size-md="2" size="3" size-sm>
                            <ion-button
                              @click="desativaCategoria(cat.id_categoria)"
                              color="danger"
                              size="small"
                            >
                              <ion-icon
                                slot="icon-only"
                                name="trash"
                              ></ion-icon>
                            </ion-button>
                          </ion-col>
                        </ion-row>
                      </ion-grid>
                    </ion-item>
                  </div>
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
import Provider from "@/services/provider";
import { toastController } from "@ionic/core";
export default {
  data() {
    return {
      nome_cat: "",
      nome_adm: "",
      foto: "",
      categorias: [],
    };
  },
  methods: {
    async efetuaCadastro() {
      if (this.nome_cat == "") {
        this.presentToast("Campo nome da categoria está em branco");
      } else {
        let dados = {
          tipo: "cad_cat",
          nm_cat: this.nome_cat,
        };
        Provider.provider("categorias", JSON.stringify(dados))
          .then((res) => {
            if (res.data.sucesso) {
              this.listaCategorias();
              this.presentToast(res.data.msg);
            } else {
              this.presentToast(res.data.msg);
            }
          })
          .catch((error) => {
            console.log("TIMEOUT " + error);
          });
      }
    },
    desativaCategoria(id) {
      let dados = {
        tipo: "del_cat",
        id: id,
      };
      Provider.provider("categorias", JSON.stringify(dados))
        .then((res) => {
          if (res.data.sucesso) {
            this.presentToast(res.data.msg);
            this.listaCategorias();
          }
        })
        .catch((error) => {
          console.log("TIMEOUT " + error);
        });
    },
    async presentToast(msg) {
      const toast = await toastController.create({
        message: msg,
        duration: 2000,
        color: "warning",
        position: "top",
        cssClass: "ion-toast",
      });
      toast.present();
    },
    listaCategorias() {
      let dados = {
        tipo: "list_cat",
      };
      Provider.provider("categorias", JSON.stringify(dados))
        .then((res) => {
          if (res.data.sucesso) {
            this.categorias = res.data.dados;
          }
        })
        .catch((error) => {
          console.log("TIMEOUT " + error);
        });
    },
    doRefresh(event) {
      var dados = JSON.parse(localStorage.getItem("isLogado"));
      this.nome_adm = dados.nm_usuario;
      this.foto = dados.foto;

      this.listaCategorias();

      setTimeout(() => {
        //console.log("Async operation has ended");
        event.target.complete();
      }, 2000);
    },
  },

  mounted() {
    var dados = JSON.parse(localStorage.getItem("isLogado"));
    this.nome_adm = dados.nm_usuario;
    this.foto = dados.foto;

    this.listaCategorias();
  },
};
</script>

<style>
#page {
  --background: rgb(55, 52, 53);
}

#form ion-input {
  font-family: "Poppins", sans-serif;
}

#form ion-label {
  font-family: "Poppins", sans-serif;
  font-weight: bold;
  color: rgb(55, 52, 53);
}
#btn_cad {
  --background: rgb(55, 52, 53);
  --background-activated: rgb(55, 52, 53);
  --background-hover: rgb(55, 52, 53);
}

.ion-toast {
  text-align: center;
}
</style>

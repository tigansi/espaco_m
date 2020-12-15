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
                    <ion-col size-md="10">
                      <ion-card-subtitle>Bem vindo(a)</ion-card-subtitle>
                      <ion-card-title>{{ nome_adm }} </ion-card-title>
                    </ion-col>
                    <ion-col>
                      <center>
                        <ion-avatar>
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
          </ion-col>

          <ion-col size="12" size-md="6">
            <ion-card style="background-color:white">
              <ion-card-content>
                <div id="form">
                  <ion-list>
                    <ion-list-header>
                      <h1>Cadastro de serviços</h1>
                    </ion-list-header>
                    <ion-item>
                      <ion-label position="floating">Nome do serviço</ion-label>
                      <IonInputVue v-model="form.nm_servico" />
                      <ion-icon slot="end" name="cut"></ion-icon>
                    </ion-item>

                    <ion-item>
                      <ion-label position="floating">Categoria</ion-label>
                      <ion-icon slot="end" name="book"></ion-icon>
                      <IonSelectVue v-model="form.nm_categoria">
                        <div
                          v-for="categoria of categorias"
                          :key="categoria.nm_categoria"
                        >
                          <ion-select-option
                            v-bind:value="categoria.nm_categoria"
                            >{{ categoria.nm_categoria }}</ion-select-option
                          >
                        </div>
                      </IonSelectVue>
                    </ion-item>

                    <ion-item>
                      <ion-label position="floating"
                        >Duração em minutos</ion-label
                      >
                      <IonInputVue v-model="form.duracao" type="number" />
                      <ion-icon slot="end" name="stopwatch"></ion-icon>
                    </ion-item>

                    <ion-item>
                      <ion-label position="floating">Valor</ion-label>
                      <IonInputVue type="number" v-model="form.valor" />
                      <ion-icon slot="end" name="cash"></ion-icon>
                    </ion-item>
                  </ion-list>
                  <ion-button @click="efetuaCadastro" size="block" id="btn_cad"
                    >Cadastrar</ion-button
                  >
                </div>
              </ion-card-content>
            </ion-card>
          </ion-col>
          <ion-col size="12" size-md="6">
            <ion-card style="background-color:white">
              <ion-card-content>
                <ion-list>
                  <ion-list-header>
                    <h1>Listagem de serviços</h1>
                  </ion-list-header>
                  <div v-for="serv of servicos" :key="serv.id_servico">
                    <ion-item>
                      <ion-grid>
                        <ion-row>
                          <ion-col size-md="10" size="9" size-sm>
                            <p>Nome: {{ serv.nm_servico }}</p>
                            <p>Categoria: {{ serv.categoria }}</p>
                            <p>Duração: {{ serv.duracao }}</p>
                            <p>Valor: {{ serv.valor }}</p>
                          </ion-col>
                          <ion-col size-md="2" size="3" size-sm>
                            <ion-button
                              @click="desativaServico(serv.id_servico)"
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
import { toastController, loadingController } from "@ionic/core";
export default {
  data() {
    return {
      nome_adm: "",
      foto: "",
      form: {
        nm_servico: "",
        nm_categoria: "",
        duracao: "",
        valor: "",
      },
      categorias: [],
      servicos: [],
    };
  },
  methods: {
    desativaServico(id) {
      let dados = {
        tipo: "del_serv",
        id: id,
      };

      Provider.provider("servicos", JSON.stringify(dados))
        .then((res) => {
          if (res.data.sucesso) {
            this.presentToast(res.data.msg);
            this.listaServicos();
          }
        })
        .catch((error) => {
          console.log("TIMEOUT " + error);
        });
    },
    async efetuaCadastro() {
      if (this.form.nm_servico == "") {
        this.presentToast("Campo nome do serviço está em branco");
      } else {
        if (this.form.nm_categoria == "") {
          this.presentToast("Campo nome da categoria está em branco");
        } else {
          if (this.form.duracao == "") {
            this.presentToast("Campo duração está em branco");
          } else {
            if (this.form.valor == "") {
              this.presentToast("Campo valor está em branco");
            } else {
              let dados = {
                tipo: "cad_serv",
                nm_servico: this.form.nm_servico,
                nm_categoria: this.form.nm_categoria,
                duracao: this.form.duracao,
                valor: this.form.valor,
              };

              const loading = await loadingController.create({
                cssClass: "my-custom-class",
                message: "Um momento...",
              });
              loading.present();

              Provider.provider("servicos", JSON.stringify(dados))
                .then((res) => {
                  console.log(res);
                  if (res.data.sucesso) {
                    loading.dismiss();
                    this.inicializa();
                    this.listaServicos();
                    this.presentToast(res.data.msg);
                  } else {
                    loading.dismiss();
                    this.presentToast(res.data.msg);
                  }
                })
                .catch((error) => {
                  loading.dismiss();
                  this.presentToast(
                    "danger",
                    "Ocorreu um erro com o servidor. Contate o suporte"
                  );
                  console.log("TIMEOUT " + error);
                });
            }
          }
        }
      }
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
    listaServicos() {
      let dados = {
        tipo: "list_serv",
      };
      Provider.provider("servicos", JSON.stringify(dados))
        .then((res) => {
          if (res.data.sucesso) {
            this.servicos = res.data.dados;
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
    inicializa() {
      this.form.nm_servico = "";
      this.form.nm_categoria = "";
      this.form.duracao = "";
      this.form.valor = "";
    },
  },
  mounted() {
    var dados = JSON.parse(localStorage.getItem("isLogado"));
    this.nome_adm = dados.nm_usuario;
    this.foto = dados.foto;
    this.listaCategorias();
    this.listaServicos();
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

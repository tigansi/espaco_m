<template>
  <ion-page>
    <ion-content id="page">
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
          <ion-col>
            <ion-card style="background-color: white">
              <ion-card-content>
                <div id="form">
                  <ion-list>
                    <ion-list-header>
                      <h1>Novo colaborador</h1>
                    </ion-list-header>
                    <ion-item>
                      <ion-label position="floating">Nome</ion-label>
                      <IonInputVue v-model="form.nome" />
                      <ion-icon slot="end" name="person"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <input
                        type="hidden"
                        v-mask="'(##) ####-#####'"
                        v-model="form.celular"
                      />
                      <ion-label position="floating">Celular</ion-label>
                      <IonInputVue type="tel" v-model="form.celular" />
                      <ion-icon slot="end" name="call"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <ion-label position="floating">E-mail</ion-label>
                      <IonInputVue v-model="form.email" type="email" />
                      <ion-icon slot="end" name="mail"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <ion-label position="stacked">Aniversário</ion-label>
                      <IonInputVue
                        v-model="form.aniversario"
                        placeholder="Coloque sua data de nascimento"
                        type="date"
                      />
                      <ion-icon slot="end" name="calendar"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <ion-label position="floating">Senha</ion-label>
                      <IonInputVue v-model="form.senha" type="password" />
                      <ion-icon slot="end" name="lock-closed"></ion-icon>
                    </ion-item>

                    <ion-item>
                      <ion-label position="floating">Tipo de usuário</ion-label>
                      <ion-icon slot="end" name="people"></ion-icon>
                      <IonSelectVue v-model="form.tipo_user">
                        <ion-select-option value="CLI"
                          >Cliente</ion-select-option
                        >
                        <ion-select-option value="COL"
                          >Colaborador</ion-select-option
                        >
                        <ion-select-option value="ADM"
                          >Administrador</ion-select-option
                        >
                      </IonSelectVue>
                    </ion-item>
                  </ion-list>

                  <br />

                  <ion-button @click="efetuaCadastro" size="block" id="btn_cad"
                    >Cadastrar</ion-button
                  >
                </div>
              </ion-card-content>
            </ion-card>
          </ion-col>
          <ion-col>
            <ion-card style="background-color: white">
              <ion-card-content>
                <div id="form">
                  <ion-list>
                    <ion-list-header>
                      <h1>Listar colaboradores</h1>
                    </ion-list-header>
                    <ion-item>
                      <ion-label position="floating">Nome</ion-label>
                      <IonInputVue v-model="form.nome" />
                      <ion-icon slot="end" name="person"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <ion-label position="floating">E-mail</ion-label>
                      <IonInputVue v-model="form.email" />
                      <ion-icon slot="end" name="mail"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <ion-label position="floating">Status</ion-label>
                      <IonSelectVue v-model="form.status">
                        <ion-select-option value="0"
                          >Demitido</ion-select-option
                        >
                        <ion-select-option value="1"
                          >Em atividade</ion-select-option
                        >
                      </IonSelectVue>
                      <ion-icon slot="end" name="checkmark-done"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <ion-label position="floating">Tipo de usuário</ion-label>
                      <IonSelectVue v-model="form.tp">
                        <ion-select-option value="CLI"
                          >Cliente</ion-select-option
                        >
                        <ion-select-option value="COL"
                          >Colaborador</ion-select-option
                        >
                        <ion-select-option value="ADM"
                          >Administrador</ion-select-option
                        >
                      </IonSelectVue>
                      <ion-icon slot="end" name="people"></ion-icon>
                    </ion-item>
                  </ion-list>
                  <br />

                  <ion-button
                    @click="efetuaPesquisa"
                    expand="block"
                    id="btn_cad"
                    >Pesquisar</ion-button
                  >
                </div>
              </ion-card-content>
            </ion-card>
          </ion-col>

          <ion-col size-md="6" size="12" size-sm>
            <div v-for="col of colaboradores" :key="col.id_usuario">
              <ion-card style="background-color: white">
                <ion-card-content>
                  <ion-list>
                    <ion-item>
                      <ion-avatar slot="start">
                        <ion-img
                          :src="
                            'http://192.168.8.7:5000/fotos?caminho=' + col.foto
                          "
                        ></ion-img>
                      </ion-avatar>
                      <ion-label>
                        <h2>{{ col.nm_usuario }}</h2>
                        <div v-if="col.nota > 0">
                          <p>Avaliação:</p>
                        </div>
                        <div v-else>
                          <p>Não há avaliações</p>
                        </div>
                        <p>{{ col.email }}</p>
                      </ion-label>
                      <div>
                        <ion-button
                          color="danger"
                          @click="efetuaDemissao(col.id_usuario, col.tipo)"
                        >
                          <ion-icon
                            size="small"
                            slot="icon-only"
                            name="person-remove"
                          ></ion-icon>
                        </ion-button>
                        <br />
                        <ion-button color="medium">
                          <ion-icon
                            size="small"
                            slot="icon-only"
                            name="information-circle"
                          ></ion-icon>
                        </ion-button>
                      </div>
                    </ion-item>
                  </ion-list>
                </ion-card-content>
              </ion-card>
            </div>
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script>
import {
  loadingController,
  toastController,
  alertController,
} from "@ionic/core";
import Provider from "@/services/provider.js";
export default {
  data() {
    return {
      form: {
        nome: "",
        email: "",
        status: "",
        tp: "",
      },
      nome_adm: "",
      foto: "",
      total: "",
      colaboradores: [],
    };
  },
  methods: {
    async efetuaDemissao(id, tipo) {
      this.confirmaDemissao(id, tipo);
    },

    async efetuaCadastro() {
      if (this.form.nome == "") {
        this.presentToast("Campo nome está em branco");
      } else {
        if (this.form.celular == "") {
          this.presentToast("Campo celular está em branco");
        } else {
          if (this.form.email == "") {
            this.presentToast("Campo e-mail está em branco");
          } else {
            if (this.form.aniversario == "") {
              this.presentToast("Campo aniversário está em branco");
            } else {
              if (this.form.senha == "" || this.form.senha.length < 6) {
                this.presentToast(
                  "Campo senha está em branco ou é muito pequena"
                );
              } else {
                if (this.form.tipo_user == "") {
                  this.presentToast("Campo tipo de usuário está em branco");
                } else {
                  let dados = {
                    tipo: "cad_usuario",
                    nome: this.form.nome,
                    celular: this.form.celular,
                    email: this.form.email,
                    aniversario: this.form.aniversario,
                    senha: this.form.senha,
                    tp: this.form.tipo_user,
                  };

                  const loading = await loadingController.create({
                    cssClass: "my-custom-class",
                    message: "Um momento...",
                  });
                  loading.present();

                  Provider.provider("usuarios", JSON.stringify(dados))
                    .then((res) => {
                      if (res.data.sucesso) {
                        //this.inicializa();
                        loading.dismiss();
                        //this.listaColaboradores();
                        this.alertaSucesso(res.data.msg, "Sucesso");
                      } else {
                        loading.dismiss();
                        this.alertaSucesso(res.data.msg, "Problemas !!!");
                      }
                    })
                    .catch((error) => {
                      loading.dismiss();
                      console.log("TIMEOUT " + error);
                    });
                }
              }
            }
          }
        }
      }
    },
    async efetuaPesquisa() {
      let dados = {
        tipo: "lista_colaboradores",
        nome: this.form.nome,
        email: this.form.email,
        status: this.form.status,
        tp: this.form.tp,
      };

      const loading = await loadingController.create({
        cssClass: "my-custom-class",
        message: "Um momento...",
      });
      loading.present();

      Provider.provider("usuarios", JSON.stringify(dados))
        .then((res) => {
          if (res.data.sucesso) {
            this.colaboradores = res.data.dados;
            this.total = res.data.total;
            loading.dismiss();

            console.log(this.colaboradores);
            this.presentToast(res.data.msg);
          } else {
            loading.dismiss();
            this.presentToast(res.data.msg);
          }
        })
        .catch((error) => {
          loading.dismiss();
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
    async alertaSucesso(msg, tipo) {
      const alert = await alertController.create({
        cssClass: "my-custom-class",
        header: tipo,
        message: msg,
        buttons: ["OK"],
      });

      await alert.present();
    },
    async confirmaDemissao(id, tipo) {
      const alert = await alertController.create({
        cssClass: "my-custom-class",
        header: "Atenção !!!",
        message: "<strong>Deseja confirmar a demissão ?</strong>",
        buttons: [
          {
            text: "Não",
            role: "cancel",
            cssClass: "secondary",
            handler: (blah) => {
              console.log("Confirm Cancel:", blah);
            },
          },
          {
            text: "Sim",
            handler: () => {
              console.log("Confirm Okay");
              let dados = {
                tipo: "desliga_user",
                id: id,
                tp: tipo,
              };
              Provider.provider("usuarios", JSON.stringify(dados))
                .then((res) => {
                  if (res.data.sucesso) {
                    this.presentToast(res.data.msg);
                    this.efetuaPesquisa();
                  } else {
                    this.presentToast(res.data.msg);
                  }
                })
                .catch((error) => {
                  console.log("TIMEOUT " + error);
                });
            },
          },
        ],
      });
      return alert.present();
    },
  },
  mounted() {
    var dados = JSON.parse(localStorage.getItem("isLogado"));
    this.nome_adm = dados.nm_usuario;
    this.foto = dados.foto;
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
</style>

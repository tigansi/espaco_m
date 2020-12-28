<template>
  <ion-page>
    <ion-content id="page">
      <ion-grid>
        <ion-row>
          <!-- -->

          <ion-col size="12" size-md="6">
            <ion-card style="background-color:white">
              <ion-card-content>
                <ion-list>
                  <ion-list-header>
                    <h1>Serviço</h1>
                  </ion-list-header>
                  <div id="form">
                    <ion-item>
                      <ion-label position="stacked">Escolha o dia</ion-label>
                      <IonInputVue type="date" v-model="form.data" />
                    </ion-item>
                    <ion-item>
                      <ion-label position="floating">Serviço</ion-label>
                      <IonSelectVue v-model="form.servico">
                        <div v-for="serv of servicos" :key="serv.id_servico">
                          <ion-select-option v-bind:value="serv.id_servico">
                            {{ serv.nm_servico }}
                          </ion-select-option>
                        </div>
                      </IonSelectVue>
                    </ion-item>

                    <ion-item>
                      <ion-label position="floating"
                        >Tempo em minutos</ion-label
                      >
                      <IonInputVue readonly v-model="form.duracao" />
                    </ion-item>
                  </div>
                </ion-list>
                <ion-button @click="buscaGrade" size="block" id="btn_cad"
                  >Grade de horários</ion-button
                >
              </ion-card-content>
            </ion-card>
            <ion-card style="background-color:white;">
              <ion-card-content>
                <ion-list>
                  <ion-list-header>
                    <h1>Grade de horários</h1>
                  </ion-list-header>
                </ion-list>
                <ion-grid>
                  <ion-row>
                    <div v-for="hor of horarios" :key="hor">
                      <ion-col size-md="2" size-sm="3">
                        <ion-button
                          style="width:125px"
                          shape="round"
                          id="btn_hor"
                          @click="escolheHorario(hor)"
                          >{{ hor }}</ion-button
                        >
                      </ion-col>
                    </div>
                  </ion-row>
                </ion-grid>
              </ion-card-content>
            </ion-card>
          </ion-col>
          <ion-col size="12" size-md="6">
            <ion-card style="background-color:white">
              <ion-card-content>
                <ion-list>
                  <ion-list-header>
                    <h1>Horários escolhidos</h1>
                  </ion-list-header>
                  <div v-for="hr_selec of hor_selecionados" :key="hr_selec">
                    <ion-item>
                      <ion-grid>
                        <ion-row>
                          <ion-col size="7" size-md="9">{{ hr_selec }}</ion-col>
                          <ion-col>
                            <ion-button
                              @click="desisteHorario(hr_selec)"
                              color="warning"
                              shape="round"
                              >Desistir</ion-button
                            >
                          </ion-col>
                        </ion-row>
                      </ion-grid>
                    </ion-item>
                  </div>
                </ion-list>
                <ion-button
                  @click="efetuaCadastroAgenda"
                  id="btn_cad"
                  expand="block"
                  >Cadastrar horários</ion-button
                >
              </ion-card-content>
            </ion-card>
            <ion-card style="background-color:white">
              <ion-card-content>
                <ion-list>
                  <ion-list-header>
                    <h1>Seus horários</h1>
                  </ion-list-header>
                  <div v-for="hr_banco of hor_banco" :key="hr_banco.id_horario">
                    <ion-item>
                      <ion-grid>
                        <ion-row>
                          <ion-col size="9" size-md="10"
                            >{{ hr_banco.data }}
                            <br />
                            <ion-card-subtitle>{{
                              hr_banco.nm_servico
                            }}</ion-card-subtitle>
                          </ion-col>
                          <ion-col>
                            <div v-if="hr_banco.is_ativo">
                              <ion-button
                                @click="deletaHorario(hr_banco.id_horario)"
                                color="danger"
                              >
                                <ion-icon
                                  slot="icon-only"
                                  name="trash"
                                ></ion-icon>
                              </ion-button>
                            </div>
                            <div v-else>
                              <ion-button color="medium">
                                <ion-icon
                                  slot="icon-only"
                                  name="check-mark-done-circle"
                                ></ion-icon>
                              </ion-button>
                            </div>
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
      id_usuario: "",
      nome_col: "",
      foto: "",
      servicos: [],
      horarios: [],
      hor_selecionados: [],
      hor_banco: [],
      form: {
        data: "",
        duracao: "",
        servico: "",
      },
    };
  },
  methods: {
    async buscaGrade() {
      if (this.form.data == "") {
        this.presentToast("Campo data em branco");
      } else {
        if (this.form.servico == "") {
          this.presentToast("Campo serviço em branco");
        } else {
          const loading = await loadingController.create({
            cssClass: "my-custom-class",
            message: "Um momento...",
          });
          loading.present();

          let dados = {
            tipo: "monta_grad_hor",
            dia: this.form.data,
            servico: this.form.servico,
            duracao: this.form.duracao,
            id_usuario: this.id_usuario,
          };

          Provider.provider("horarios", JSON.stringify(dados))
            .then((res) => {
              if (res.data.sucesso) {
                console.log(res.data.dados);
                this.horarios = res.data.dados;
                loading.dismiss();
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
        }
      }
    },
    escolheHorario(hor) {
      var index = this.horarios.indexOf(hor);
      if (index > -1) {
        this.horarios.splice(index, 1);
      }

      this.hor_selecionados.push(hor);
    },
    desisteHorario(hor) {
      var index = this.hor_selecionados.indexOf(hor);
      if (index > -1) {
        this.hor_selecionados.splice(index, 1);
      }
      this.buscaGrade();
    },
    deletaHorario(id_hor) {
      console.log(id_hor);
      let dados = {
        tipo: "deleta_hor",
        id_hor: id_hor,
      };
      Provider.provider("horarios", JSON.stringify(dados))
        .then((res) => {
          if (res.data.sucesso) {
            this.hor_banco = [];
            this.listaHorarios();
            this.presentToast(res.data.msg);
          } else {
            this.presentToast(res.data.msg);
          }
        })
        .catch((error) => {
          console.log("TIMEOUT " + error);
        });
    },
    efetuaCadastroAgenda() {
      let dados = {
        tipo: "cad_hor",
        id_usuario: this.id_usuario,
        servico: this.form.servico,
        dia: this.form.data,
        hor_selecionados: this.hor_selecionados,
      };
      Provider.provider("horarios", JSON.stringify(dados))
        .then((res) => {
          if (res.data.sucesso) {
            this.horarios = [];
            this.hor_selecionados = [];
            this.listaHorarios();
            this.presentToast(res.data.msg);
          }
        })
        .catch((error) => {
          console.log("TIMEOUT " + error);
        });
    },
    listaHorarios() {
      let dados = {
        tipo: "list_hor",
        id_usuario: this.id_usuario,
      };
      Provider.provider("horarios", JSON.stringify(dados))
        .then((res) => {
          if (res.data.sucesso) {
            this.hor_banco = res.data.dados;
          } else {
            console.log(res.data.msg);
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
  },
  mounted() {
    var dados = JSON.parse(localStorage.getItem("isLogado"));
    this.nome_col = dados.nm_usuario;
    this.foto = dados.foto;
    this.id_usuario = dados.id_usuario;
    this.listaServicos();
    this.listaHorarios();
  },

  updated() {
    for (let i of this.servicos) {
      //console.log(i.duracao);
      if (this.form.servico == i.id_servico) {
        this.form.duracao = i.duracao;
      }
    }
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

#btn_hor {
  --background: rgb(60, 187, 178);
  --background-activated: rgb(60, 187, 178);
  --background-hover: rgb(60, 187, 178);
}

.ion-toast {
  text-align: center;
}
</style>

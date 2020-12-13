<template>
  <ion-page>
    <ion-header>
      <ion-toolbar id="page" style="color:white">
        <ion-buttons slot="start">
          <ion-menu-button></ion-menu-button>
        </ion-buttons>
        <ion-title>Meu perfil</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content id="page">
      <ion-grid>
        <ion-row>
          <ion-col size="12" size-sm>
            <ion-card style="background-color:white">
              <ion-card-content>
                <div id="form">
                  <ion-list>
                    <ion-list-header>
                      <h1>Dados pessoais</h1>
                      <center>
                        <ion-avatar>
                          <ion-img
                            :src="
                              'http://192.168.8.7:5000/fotos?caminho=' + caminho
                            "
                          ></ion-img>
                        </ion-avatar>
                        <br />
                      </center>
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
                      <IonInputVue readonly v-model="form.email" type="email" />
                      <ion-icon slot="end" name="mail"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <ion-label position="stacked">Aniversário</ion-label>
                      <IonInputVue v-model="form.aniversario" />
                      <ion-icon slot="end" name="calendar"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <ion-label position="floating">Senha</ion-label>
                      <IonInputVue v-model="form.senha" type="password" />
                      <ion-icon slot="end" name="lock-closed"></ion-icon>
                    </ion-item>
                    <ion-item>
                      <br />
                      <input type="file" @change="previewFiles" />
                      <ion-icon slot="end" name="image"></ion-icon>
                    </ion-item>
                  </ion-list>

                  <br />

                  <ion-button @click="alteraDados" size="block" id="btn_cad"
                    >Cadastrar</ion-button
                  >
                </div>
              </ion-card-content>
            </ion-card>
          </ion-col>
          <ion-col>
            <ion-card style="background-color:white">
              <ion-card-content>
                <div id="form">
                  <ion-list>
                    <ion-list-header>
                      <h1>Cartão de crédito</h1>
                    </ion-list-header>
                  </ion-list>

                  <br />

                  <ion-button
                    id="btn-cadastrar-cartao"
                    expand="full"
                    shape="round"
                    >Cadastrar cartão de crédito</ion-button
                  >
                </div>
              </ion-card-content>
            </ion-card>
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script>
import { loadingController, alertController } from "@ionic/core";
import Provider from "@/services/provider.js";
export default {
  data() {
    return {
      form: {
        id: "",
        nome: "",
        celular: "",
        aniversario: "",
        senha: "",
        foto_user: "",
      },
      caminho: "",
    };
  },
  methods: {
    async alteraDados() {
      if (this.form.senha != "") {
        if (this.form.senha.length < 6) {
          this.alertaSucesso("A senha deve ser maior", "Atenção !!!");
          this.form.senha = "";
          return;
        }
      }

      let dados = {
        nome: this.form.nome,
        celular: this.form.celular,
        aniversario: this.form.aniversario,
        senha: this.form.senha,
        id: this.form.id,
      };

      const dados_user = new FormData();
      if (this.form.foto_user == "" || this.form.foto_user == null) {
        dados_user.append("dados", JSON.stringify(dados));
      } else {
        dados_user.append("dados", JSON.stringify(dados));
        dados_user.append(
          "foto_user",
          this.form.foto_user,
          this.form.foto_user.name
        );
      }
      const loading = await loadingController.create({
        cssClass: "my-custom-class",
        message: "Um momento...",
      });
      loading.present();
      Provider.provider("altera_dados", dados_user)
        .then((res) => {
          if (res.data.sucesso) {
            dados_user.delete("dados");
            dados_user.delete("foto_user");
            localStorage.clear();
            localStorage.setItem("isLogado", JSON.stringify(res.data.dados[0]));
            this.inicializa();
            loading.dismiss();
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
    },
    previewFiles(event) {
      //console.log(event);
      this.form.foto_user = event.target.files[0];
      console.log(this.form.foto_user);
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
    inicializa() {
      var dados = JSON.parse(localStorage.getItem("isLogado"));
      this.form.id = dados.id_usuario;
      this.form.nome = dados.nm_usuario;
      this.form.celular = dados.celular;
      this.form.email = dados.email;
      this.form.aniversario = dados.aniversario;
      this.caminho = dados.foto;
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

#btn-cadastrar-cartao {
  --background: rgb(60, 187, 178);
  --background-activated: rgb(60, 187, 178);
  --background-hover: rgb(60, 187, 178);
}

.ion-toast {
  text-align: center;
}

#avatar {
  width: 70px;
}
</style>

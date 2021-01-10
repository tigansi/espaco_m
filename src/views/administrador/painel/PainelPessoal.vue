<template>
  <ion-app>
    <ion-header>
      <ion-toolbar id="page" style="color: white">
        <ion-buttons slot="start">
          <ion-menu-button></ion-menu-button>
        </ion-buttons>
        <ion-title>Administrador</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content>
      <ion-tabs>
        <ion-tab tab="CadastrarPessoas" :routes="['CadastrarPessoas']">
          <CadastrarPessoas />
        </ion-tab>
        <ion-tab tab="ListagemPessoas" :routes="['ListagemPessoas']">
          <ListagemPessoas />
        </ion-tab>

        <ion-tab-bar slot="bottom">
          <ion-tab-button
            tab="CadastrarPessoas"
            class="btn-tab"
            :to="{ name: 'CadastrarPessoas' }"
          >
            <ion-icon name="home"></ion-icon>
            <ion-label>Salão</ion-label>
          </ion-tab-button>

          <ion-tab-button
            tab="ListagemPessoas"
            class="btn-tab"
            :to="{ name: 'ListagemPessoas' }"
          >
            <ion-icon name="people"></ion-icon>
            <ion-label>Pessoal</ion-label>
          </ion-tab-button>
        </ion-tab-bar>
      </ion-tabs>
    </ion-content>
  </ion-app>
</template>

<script>
import CadastrarPessoas from "./tabsPessoal/CadastrarPessoas";
import ListagemPessoas from "./tabsPessoal/ListagemPessoas";

export default {
  components: {
    CadastrarPessoas,
    ListagemPessoas,
  },
};
</script>

<style>
#page {
  --background: rgb(55, 52, 53);
}

ion-tab-bar {
  --color: white;
  --background: rgb(55, 52, 53);
}

ion-tab-button.btn-tab {
  --color-selected: rgb(253, 243, 205);
}
</style>

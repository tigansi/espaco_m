<template>
  <ion-page>
    <ion-header>
      <ion-toolbar id="page" style="color:white">
        <ion-buttons slot="start">
          <ion-menu-button></ion-menu-button>
        </ion-buttons>
        <ion-title>Administrador</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content >
      <ion-tabs>
        <ion-tab tab="CadastrarServicos" :routes="['CadastrarServicos']">
          <CadastrarServicos />
        </ion-tab>
        <ion-tab tab="CadastrarCategorias" :routes="['CadastrarCategorias']">
          <CadastrarCategorias />
        </ion-tab>

        <ion-tab-bar slot="bottom">
          <ion-tab-button
            tab="CadastrarCategorias"
            class="btn-tab"
            :to="{ name: 'CadastrarCategorias' }"
          >
            <ion-icon name="book"></ion-icon>
            <ion-label>Cadastrar categorias</ion-label>
          </ion-tab-button>

          <ion-tab-button
            tab="CadastrarServicos"
            class="btn-tab"
            :to="{ name: 'CadastrarServicos' }"
          >
            <ion-icon name="cut"></ion-icon>
            <ion-label>Cadastrar Serviços</ion-label>
          </ion-tab-button>
        </ion-tab-bar>
      </ion-tabs>
    </ion-content>
  </ion-page>
</template>

<script>
import CadastrarServicos from "./tabsServicos/CadastrarServicos";
import CadastrarCategorias from "./tabsServicos/CadastrarCategorias";
export default {
  components: {
    CadastrarServicos,
    CadastrarCategorias,
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

<template>
  <ion-app main>
    <ion-header>
      <ion-toolbar id="page" style="color:white">
        <ion-buttons slot="start">
          <ion-menu-button></ion-menu-button>
        </ion-buttons>
        <ion-title>Clientes</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content>
      <ion-tabs>
        <ion-tab tab="Agendar" :routes="['Agendar']">
          <Agendar />
        </ion-tab>
        <ion-tab tab="Profissionais" :routes="['Profissionais']">
          <Profissionais />
        </ion-tab>
        <ion-tab tab="Servicos" :routes="['Servicos']">
          <Servicos />
        </ion-tab>

        <ion-tab-bar slot="bottom">
          <ion-tab-button
            tab="Agendar"
            class="btn-tab"
            :to="{ name: 'Agendar' }"
          >
            <ion-icon name="calendar"></ion-icon>
            <ion-label>Agendamentos</ion-label>
          </ion-tab-button>

          <ion-tab-button
            tab="Profissionais"
            class="btn-tab"
            :to="{ name: 'Profissionais' }"
          >
            <ion-icon name="people"></ion-icon>
            <ion-label>Profissionais</ion-label>
          </ion-tab-button>

          <ion-tab-button
            tab="Servicos"
            class="btn-tab"
            :to="{ name: 'Servicos' }"
          >
            <ion-icon name="book"></ion-icon>
            <ion-label>Servicos</ion-label>
          </ion-tab-button>
        </ion-tab-bar>
      </ion-tabs>
    </ion-content>
  </ion-app>
</template>

<script>
import Agendar from "./tabs/Agendar";
import Profissionais from "./tabs/Profissionais";
import Servicos from "./tabs/Servicos";

export default {
  components: {
    Agendar,
    Profissionais,
    Servicos,
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

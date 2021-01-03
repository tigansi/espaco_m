<template>
  <ion-app>
    <ion-header>
      <ion-toolbar id="page" style="color:white">
        <ion-buttons slot="start">
          <ion-menu-button></ion-menu-button>
        </ion-buttons>
        <ion-title>Colaborador</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content>
      <ion-tabs>
        <ion-tab tab="Agenda" :routes="['Agenda']">
          <Agenda />
        </ion-tab>
        <ion-tab tab="ConfigAgenda" :routes="['ConfigAgenda']">
          <ConfigAgenda />
        </ion-tab>

        <ion-tab-bar slot="bottom">
          <ion-tab-button tab="Agenda" :to="{ name: 'Agenda' }" class="btn-tab">
            <ion-icon name="calendar"></ion-icon>
            <ion-label>Agenda do dia</ion-label>
          </ion-tab-button>

          <ion-tab-button
            tab="ConfigAgenda"
            class="btn-tab"
            :to="{ name: 'ConfigAgenda' }"
          >
            <ion-icon name="settings"></ion-icon>
            <ion-label>Configurar horários</ion-label>
          </ion-tab-button>
        </ion-tab-bar>
      </ion-tabs>
    </ion-content>
  </ion-app>
</template>

<script>
import ConfigAgenda from "./tabsAgenda/ConfigAgenda";
import Agenda from "./tabsAgenda/Agenda";

export default {
  components: {
    ConfigAgenda,
    Agenda,
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

<template>
  <div class="ion-page">
    <ion-content>
      <ion-split-pane content-id="main">
        <MenuColaborador />
        <ion-vue-router id="main"></ion-vue-router>
      </ion-split-pane>
    </ion-content>
  </div>
</template>

<script>
import MenuColaborador from "@/components/MenuColaborador";
import { addIcons } from "ionicons";
import { exit, settings, calendar, person, trash } from "ionicons/icons";

addIcons({
  "md-exit": exit,
  "ios-exit": exit,
  "md-settings": settings,
  "ios-settings": settings,
  "md-calendar": calendar,
  "ios-calendar": calendar,
  "md-person": person,
  "ios-person": person,
  "md-trash": trash,
  "ios-trash": trash,
});

export default {
  components: {
    MenuColaborador,
  },
};
</script>

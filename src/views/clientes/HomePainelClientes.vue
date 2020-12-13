<template>
  <div class="ion-page">
    <ion-content>
      <ion-split-pane content-id="main">
        <MenuCliente />
        <ion-vue-router id="main"></ion-vue-router>
      </ion-split-pane>
    </ion-content>
  </div>
</template>

<script>
import { addIcons } from "ionicons";
import {
  person,
  calendar,
  exit,
  home,
  people,
  book,
  lockClosed,
  call,
  mail,
  image,
} from "ionicons/icons";
addIcons({
  "md-person": person,
  "ios-person": person,
  "md-calendar": calendar,
  "ios-calendar": calendar,
  "md-exit": exit,
  "ios-exit": exit,
  "md-home": home,
  "ios-home": home,
  "md-people": people,
  "ios-people": people,
  "md-book": book,
  "ios-book": book,
  "md-lock-closed": lockClosed,
  "ios-lock-closed": lockClosed,
  "md-call": call,
  "ios-call": call,
  "md-mail": mail,
  "ios-mail": call,
  "md-image": image,
  "ios-image": image,
});

import MenuCliente from "@/components/MenuCliente";

export default {
  components: {
    MenuCliente,
  },
};
</script>

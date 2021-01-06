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
  calendarClear,
  exit,
  home,
  people,
  book,
  lockClosed,
  call,
  mail,
  image,
  informationCircle,
  star,
} from "ionicons/icons";
addIcons({
  "md-person": person,
  "ios-person": person,
  "md-calendar": calendar,
  "ios-calendar": calendar,
  "md-calendar-clear": calendarClear,
  "ios-calendar-clear": calendarClear,
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
  "md-information-circle": informationCircle,
  "ios-information-circle": informationCircle,
  "md-star": star,
  "ios-star": star,
});

import MenuCliente from "@/components/MenuCliente";

export default {
  components: {
    MenuCliente,
  },
};
</script>

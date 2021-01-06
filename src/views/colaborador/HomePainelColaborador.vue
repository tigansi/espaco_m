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
import {
  exit,
  settings,
  calendar,
  person,
  trash,
  image,
  lockClosed,
  mail,
  call,
  checkmarkDoneCircle,
  play,
  stop,
  chevronDownCircleOutline,
  informationCircle,
  star
} from "ionicons/icons";

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
  "md-image": image,
  "ios-image": image,
  "md-lock-closed": lockClosed,
  "ios-lock-closed": lockClosed,
  "md-mail": mail,
  "ios-mail": mail,
  "md-call": call,
  "ios-call": call,
  "md-check-mark-done-circle": checkmarkDoneCircle,
  "ios-check-mark-done-circle": checkmarkDoneCircle,
  "md-play": play,
  "ios-play": play,
  "md-stop": stop,
  "ios-stop": stop,
  "md-chevron-down-circle-outline": chevronDownCircleOutline,
  "ios-chevron-down-circle-outline": chevronDownCircleOutline,
  "md-information-circle": informationCircle,
  "ios-information-circle": informationCircle,
  "md-star": star,
  "ios-star": star,
});

export default {
  components: {
    MenuColaborador,
  },
};
</script>

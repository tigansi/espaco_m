<template>
  <div class="ion-page">
    <ion-content>
      <ion-split-pane content-id="main">
        <MenuAdm />
        <ion-vue-router id="main"></ion-vue-router>
      </ion-split-pane>
    </ion-content>
  </div>
</template>

<script>
import MenuAdm from "@/components/MenuAdm";
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
  barChart,
  addCircle,
  checkmarkDone,
  personAdd,
  personRemove,
  cut,
  trash,
  stopwatch,
  cash,
  informationCircle,
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
  "md-bar-chart": barChart,
  "ios-bar-chart": barChart,
  "md-add-circle": addCircle,
  "ios-add-circle": addCircle,
  "md-checkmark-done": checkmarkDone,
  "ios-checkmark-done": checkmarkDone,
  "md-person-add": personAdd,
  "ios-person-add": personAdd,
  "md-person-remove": personRemove,
  "ios-person-remove": personRemove,
  "md-cut": cut,
  "ios-cut": cut,
  "md-trash": trash,
  "ios-trash": trash,
  "md-stopwatch": stopwatch,
  "ios-stopwatch": stopwatch,
  "md-cash": cash,
  "ios-cash": cash,
  "md-information-circle": informationCircle,
  "ios-information-circle": informationCircle,
});
export default {
  components: {
    MenuAdm,
  },
};
</script>

import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Ionic from "@ionic/vue";
import "@ionic/core/css/ionic.bundle.css";
import VueMask from "v-mask";
import { VueMaskDirective } from "v-mask";
import { VueMaskFilter } from "v-mask";

Vue.config.productionTip = false;

Vue.use(Ionic);
Vue.directive("mask", VueMaskDirective);
Vue.filter("VMask", VueMaskFilter);
Vue.use(VueMask);

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");

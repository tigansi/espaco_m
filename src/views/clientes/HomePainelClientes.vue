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
import MenuCliente from "@/components/MenuCliente";

export default {
  components: {
    MenuCliente,
  },
};
</script>

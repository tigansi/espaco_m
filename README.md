# Espaço M 

É um aplicativo de agendamento para o salão Espaço M

## Configurações do Vue
* Para criar o projeto a primeira vez, é necessário seguir alguns passos, após criar o projeto Vue
    * vue add router # com o history mode habilitado;
    * Rodar o npm install --save axios vue-axios;
    * Rodar o npm install v-mask;
    * Rodar o npm i vue-star-rating;

## Configurações do Ionic
* Para criar o projeto a primeira vez, é necessário seguir alguns passos, após criar o projeto Vue
    * Rodar o npm install @ionic/core;
    * Rodar o npm install @ionic/vue@0.0.9;
    * Rodar o npm install ionicons(Instala os icones do IONIC);

## Configuração do android
* Para criar o projeto a primeira vez, deve seguir os passos abaixo.
    * Rodar npm install @capacitor/core @capacitor/cli;
    * Rodar o npm run build;
    * Ir no arquivo capacitor.config.json e mudar a linha para o que está abaixo:
        * "webDir": "dist"
    * Rodar npx cap add android;
    * Rodar npx cap copy;
    * Rodar npx cap sync;
    * Rodar npx cap open android;
    * Para conseguir se conectar ao banco local, no arquivo AndroidManifest.xml, que fica localizado em, app/src/main/AndroidManifest.xml, deve ser colocada a linha android:usesCleartextTraffic="true", na tag application.

## Configurações no Projeto
* Em src/main.js, deve ser incluida as seguintes linhas:
	* import Ionic from "@ionic/vue";
	* import "@ionic/core/css/ionic.bundle.css";
	* import VueMask from "v-mask";
	* import { VueMaskDirective } from "v-mask";
	* import { VueMaskFilter } from "v-mask";
	* Vue.use(Ionic);
	* Vue.directive("mask", VueMaskDirective);
	* Vue.filter("VMask", VueMaskFilter);
	* Vue.use(VueMask);
* Em src/router/index.js:
	* import { IonicVueRouter } from "@ionic/vue";
	* Vue.use(IonicVueRouter);
	* Na parte de baixo, onde existe o VueRouter, deve trocar ele por IonicVueRouter
* Em App.vue, deve se apagar tudo e colocar <template><ion-vue-router></ion-vue-router></template>
* Na pasta pubilic/index.html, para evitar problemas de liguagem, deve se colocar pt-br na tag de liguagem
* No mesmo lugar acima, no index.html, <!DOCTYPE html mode="ios"> ou <!DOCTYPE html mode="md"> para escolher entre Android e IOS, se deixar em branco, o sistema escolhe automáticamente

## Input's VueJS e Ionic
* Para usar os inputs do Ionic com o vue, é necessário consultar as informações no final da página abaixo:
    * https://programmer.help/blogs/v-model-and-ionic4-component-data-binding-failed.html
* Para trabalhar com sistema de estrelas de avaliação é necessário seguir as instruções
    * https://www.npmjs.com/package/vue-star-rating


## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

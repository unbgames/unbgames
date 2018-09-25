import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Game from "./views/Game.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/game/:game_id",
      name: "game",
      component: Game,
      props: route => {
        return { game_id: Number(route.params.game_id) };
      },
    }
  ],
  scrollBehavior () {
    return { x: 0, y: 0 }
  }
});

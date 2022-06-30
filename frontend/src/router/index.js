/* eslint-disable */
import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AccountView from "../views/AccountView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/account",
      name: "account",
      redirect: {name: 'dashboard'},
      component: AccountView,
      children: [
        {
          path: '/account/dashboard',
          name: 'dashboard',
          component: () => import("../components/AppAccountDashboard.vue")
        },
        {
          path: '/account/profile',
          name: 'myprofile',
          component: () => import("../components/AppAccountProfile.vue")
        },
        {
          path: '/account/deposit',
          name: 'deposit',
          component: () => import("../components/AppAccountDeposit.vue")
        },
        {
          path: '/account/withdrawal',
          name: 'withdrawal',
          component: () => import("../components/AppAccountWithdrawal.vue")
        },
        {
          path: '/account/copy-expert',
          name: 'copyexpert',
          component: () => import("../components/AppAccountCopyExpert.vue")
        },
        {
          path: '/account/referral',
          name: 'referral',
          component: () => import("../components/AppAccountReferral.vue")
        },
        {
          path: '/account/settings',
          name: 'settings',
          component: () => import("../components/AppAccountProfile.vue")
        },
      ]
    },
    {
      path: "/signin",
      name: "signin",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/SignInView.vue"),
    },
    {
      path: "/forgot-password",
      name: "forgotpassword",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/ForgotPasswordView.vue"),
    },
    {
      path: "/signup",
      name: "signup",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/SignUpView.vue"),
    },
  ],
});

export default router;

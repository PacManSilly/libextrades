/* eslint-disable */
import { createRouter, createWebHistory, useRouter } from "vue-router";
import { useUserStore } from '../stores/user';
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
      meta: {requiresAuth: true},
      component: AccountView,
      children: [
        {
          path: '/account/dashboard',
          name: 'dashboard',
          component: () => import("../components/AppAccountDashboard.vue")
        },
        {
          path: '/account/myprofile',
          name: 'myprofile',
          component: () => import("../components/AppAccountProfile.vue")
        },
        {
          path: '/account/deposit',
          name: 'deposit',
          redirect: {name: 'deposithistory'},
          component: () => import("../components/AppAccountDeposit.vue"),
          children: [
            {
              path: '',
              name: 'deposithistory',
              component: () => import("../components/AppAccountDepositHistory.vue"),
            },
            {
              path: '/account/deposit/investments/plans',
              name: 'investmentplan',
              component: () => import("../components/AppAccountInvestmentPlan.vue"),
            },
          ]
        },
        {
          path: '/account/withdrawal',
          name: 'withdrawal',
          redirect: {name: 'withrawalhistory'},
          component: () => import("../components/AppAccountWithdrawal.vue"),
          children: [
            {
              path: '',
              name: 'withrawalhistory',
              component: () => import("../components/AppAccountWithdrawalHistory.vue"),
            },
            {
              path: '/account/withdrawal/methods',
              name: 'withrawalmethods',
              component: () => import("../components/AppAccountWithdrawalMethod.vue"),
            },
          ]
        },
        {
          path: '/account/copyexpert',
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
          component: () => import("../components/AppAccountSetting.vue")
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

router.beforeEach((to, from) => {
  const user = useUserStore()

  if (to.meta.requiresAuth && !JSON.parse(localStorage.getItem('libex_token'))) {
    user.userSignIn.redirect = to.fullPath
    return {name: 'signin', query: {redirect: to.fullPath}}
  }
})

export default router;

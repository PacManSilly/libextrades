/* eslint-disable */
import { createRouter, createWebHistory, useRouter } from "vue-router";
import { useUserStore } from '../stores/user';
import HomeView from "../views/HomeView.vue";
import AccountView from "../views/AccountView.vue";
import NotFoundView from "../views/NotFoundView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      meta: {title: "LibExTrades | Welcome"},
    },
    {
      path: "/trade",
      name: "trade",
      redirect: {name: 'tradeforex'},
      component: () => import("../views/TradeExplain.vue"),
      children: [
        {
          path: '/trade/forex',
          name: 'tradeforex',
          component: () => import("../components/AppTradeForex.vue"),
          meta: {title: "LibExTrades | Trade Forex"},
        },
        {
          path: '/trade/stock',
          name: 'tradestock',
          component: () => import("../components/AppTradeStock.vue"),
          meta: {title: "LibExTrades | Trade Stocks"},
        },
        {
          path: '/trade/crypto',
          name: 'tradecrypto',
          component: () => import("../components/AppTradeCrypto.vue"),
          meta: {title: "LibExTrades | Trade Cryptos"},
        },
        {
          path: '/trade/option',
          name: 'tradeoption',
          component: () => import("../components/AppTradeOption.vue"),
          meta: {title: "LibExTrades | Trade Options"},
        },
        {
          path: '/trade/copytrader',
          name: 'tradecopytrader',
          component: () => import("../components/AppTradeCopyTrader.vue"),
          meta: {title: "LibExTrades | Copy Trading"},
        },
      ]
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
          component: () => import("../components/AppAccountDashboard.vue"),
          meta: {title: "LibExTrades | Dasboard"},
        },
        {
          path: '/account/myprofile',
          name: 'myprofile',
          component: () => import("../components/AppAccountProfile.vue"),
          meta: {title: "LibExTrades | Profile"},
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
              meta: {title: "LibExTrades | My Deposits"},
            },
            {
              path: '/account/deposit/investments/plans',
              name: 'investmentplan',
              component: () => import("../components/AppAccountInvestmentPlan.vue"),
              meta: {title: "LibExTrades | Investment Plans"},
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
              meta: {title: "LibExTrades | My Withdrawals"},
            },
            {
              path: '/account/withdrawal/methods',
              name: 'withrawalmethods',
              component: () => import("../components/AppAccountWithdrawalMethod.vue"),
              meta: {title: "LibExTrades | Withdrawal Methods"},
            },
          ]
        },
        {
          path: '/account/copyexpert',
          name: 'copyexpert',
          redirect: {name: 'mytraders'},
          component: () => import("../components/AppAccountCopyExpert.vue"),
          children: [
            {
              path: '',
              name: 'mytraders',
              component: () => import("../components/AppAccountMyTraders.vue"),
              meta: {title: "LibExTrades | My Traders"},
            },
            {
              path: '/account/copyexpert/traders',
              name: 'experttraders',
              component: () => import("../components/AppAccountExpertTraders.vue"),
              meta: {title: "LibExTrades | Expert Traders"},
            }
          ]
        },
        {
          path: '/account/referral',
          name: 'referral',
          component: () => import("../components/AppAccountReferral.vue"),
          meta: {title: "LibExTrades | Referrals"},
        },
        {
          path: '/account/settings',
          name: 'settings',
          component: () => import("../components/AppAccountSetting.vue"),
          meta: {title: "LibExTrades | Settings"},
        },
      ]
    },
    {
      path: "/signin",
      name: "signin",
      component: () => import("../views/SignInView.vue"),
      meta: {title: "LibExTrades | Sign In"},
    },
    {
      path: "/forgot-password",
      name: "forgotpassword",
      component: () => import("../views/ForgotPasswordView.vue"),
      meta: {title: "LibExTrades | Forgot Password"},
    },
    {
      path: "/password/reset/confirm/:uid/:token",
      name: "resetpassword",
      component: () => import("../views/ResetPasswordView.vue"),
      props: true,
      meta: {title: "LibExTrades | Reset Password"},

    },
    {
      path: "/verify-account/email/",
      name: "verifyaccount",
      component: () => import("../views/VerifyAccountView.vue"),
      meta: {title: "LibExTrades | Verify Account"},
    },
    {
      path: "/signup",
      name: "signup",
      component: () => import("../views/SignUpView.vue"),
      meta: {title: "LibExTrades | Sign Up"},
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'notfound',
      component: NotFoundView,
      meta: {title: "LibExTrades | 404 | Not Found"},
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) return {el: to.hash,  behavior: "smooth"}
    else return { top: 0, behavior: "smooth" }
  }
});

router.beforeEach((to, from) => {
  // update the page title
  document.title = to.meta.title;
  const user = useUserStore()

  if (to.meta.requiresAuth && !JSON.parse(localStorage.getItem('libex_token'))) {
    user.userSignIn.redirect = to.fullPath
    return {name: 'signin', query: {redirect: to.fullPath}}
  }
})


export default router;

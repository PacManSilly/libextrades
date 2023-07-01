<script setup>
/* eslint-disable */
import AppTopNav from '../components/AppTopNav.vue';
import AppHomeFooter from '../components/AppHomeFooter.vue';
import AppHomeContactUs from '../components/AppHomeContactUs.vue';
import IconCheckAll from '../components/icons/IconCheckAll.vue';
import teamImg from '../assets/images/team.jpg'
</script>

<template>
  <div class="w-full h-full min-h-full">

    <nav class="fixed top-0 right-0 w-full">
      <AppTopNav />
    </nav>

    <div class="w-11/12 mx-auto flex flex-col gap-y-16 pt-32 pb-20 lg:pt-44 lg:w-9/12">

      <div class="flex flex-col items-center gap-y-10 lg:flex-row">

        <!-- start of about text -->
        <div class="flex-1 flex flex-col items-start gap-y-5 lg:pr-10">
          <p class="bg-red-600 text-white text-xs px-4 py-2 rounded-md">About Us</p>
          <h3 class="text-2xl text-slate-100 font-black md:text-4xl">
            Our investment platform was built from the ground up.
          </h3>
          <p class="text-slate-500 text-sm font-normal md:text-base">
            LibExTrades has been one of the leading online brokers since 2014. Our developers, financial experts,
            personal, and support managers are making every effort to make your investment/trading more comfortable
            and profitable year after year. All associates join via the easy and affordable link registration which
            will establish a powerful international alliance for world trade.
          </p>
          <div class="flex text-slate-700 gap-5">
            <div>
              <p class="text-2xl font-black md:text-4xl">8</p>
              <p class="text-xs font-normal md:text-sm">Years of<br>experience</p>
            </div>

            <div>
              <p class="text-2xl font-black md:text-4xl">2K+</p>
              <p class="text-xs font-normal md:text-sm">Satisfied and<br>happy investors</p>
            </div>

            <div>
              <p class="text-2xl font-black md:text-4xl">$1.2</p>
              <p class="text-xs font-normal md:text-sm">Investors deposit</p>
            </div>

            <div>
              <p class="text-2xl font-black md:text-4xl">$2.3M</p>
              <p class="text-xs font-normal md:text-sm">Paid to investors</p>
            </div>
          </div>
        </div>
        <!-- end of about text -->

        <!-- start of about image -->
        <div class="flex-1">
          <img :src="teamImg" class="w-full object-cover object-center rounded-md shadow-md shadow-slate-800">
        </div>
        <!-- end of about image -->

      </div>

      <div class="grid grid-cols-1 gap-10 md:grid-cols-2 lg:grid-cols-3">

        <div class="flex flex-col gap-5">
          <div class="w-12 h-12 flex items-center justify-center rounded-full bg-slate-700 shadow-inner shadow-black">
            <IconCheckAll class="w-7 h-7 fill-slate-300" />
          </div>
          <p class="text-xs text-slate-500 font-normal md:text-sm">
            LibExTrades is an advanced investment platform based in 701 Sheppard Ave W, North York, ON M3H 2S7, Canada.
            It was established February 2014. We are strictly into trading, mining with lots of investment and assets in paid
            adverts, HYIPs, ICOs, Forex also buying signals from big exchanges.
          </p>
        </div>

        <div class="flex flex-col gap-5">
          <div class="w-12 h-12 flex items-center justify-center rounded-full bg-slate-700 shadow-inner shadow-black">
            <IconCheckAll class="w-7 h-7 fill-slate-300" />
          </div>
          <p class="text-xs text-slate-500 font-normal md:text-sm">
            LibExTrades vision is to build a strong alliance and everlasting partnership with our investors,also leading them to
            financial Independence. Our software system was developed to give our investors around the world a profit with varying
            ROI depending on the amount of funds invested.
          </p>
        </div>

        <div class="flex flex-col gap-5">
          <div class="w-12 h-12 flex items-center justify-center rounded-full bg-slate-700 shadow-inner shadow-black">
            <IconCheckAll class="w-7 h-7 fill-slate-300" />
          </div>
          <p class="text-xs text-slate-500 font-normal md:text-sm">
            All investors from any country will share business ideas and the most important part of it, in a certain way, the profits
            will be directly distributed to all LibExTrades associates worldwide. You get 10% from any deposit made by your direct
            referral.
          </p>
        </div>

      </div>

    </div>

    <AppHomeContactUs />
    <AppHomeFooter />

  </div>
</template>


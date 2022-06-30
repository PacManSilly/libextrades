<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
import AppLogoVue from './AppLogo.vue';
import IconHome from './icons/IconHome.vue';
import IconUser from './icons/IconUser.vue';
import IconTrendingDown from './icons/IconTrendingDown.vue';
import IconTrendingUp from './icons/IconTrendingUp.vue';
import IconRefresh from './icons/IconRefresh.vue';
import IconGroup from './icons/IconGroup.vue';
import IconSetting from './icons/IconSetting.vue';
</script>

<template>
    <div class="w-full h-screen">

        <div class="w-full h-full flex flex-col overflow-y-auto gap-10 items-center bg-slate-800 py-20">

            <!-- start of logo -->
            <div>
                <AppLogoVue />
            </div>

            <div class="flex flex-col">
                <!-- dashboard link -->
                <RouterLink :to="{name: 'home'}" active-class="bg-slate-900 text-slate-100" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-sm hover:bg-slate-900">
                    <IconHome class="w-7 h-7 fill-slate-600 group-hover:fill-slate-100" />
                    <p class="self-end text-slate-600 group-hover:text-slate-100">Dashboard</p>
                </RouterLink>
                <!-- my profile link -->
                <RouterLink :to="{name: 'home'}" active-class="bg-slate-900 text-slate-100" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-sm hover:bg-slate-900">
                    <IconUser class="w-7 h-7 fill-slate-600 group-hover:fill-slate-100" />
                    <p class="self-end text-slate-600 group-hover:text-slate-100">My Profile</p>
                </RouterLink>
                <!-- deposit link -->
                <RouterLink :to="{name: 'home'}" active-class="bg-slate-900 text-slate-100" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-sm hover:bg-slate-900">
                    <IconTrendingDown class="w-7 h-7 fill-slate-600 group-hover:fill-slate-100" />
                    <p class="self-end text-slate-600 group-hover:text-slate-100">Deposit</p>
                </RouterLink>
                <!-- withdrawal link -->
                <RouterLink :to="{name: 'home'}" active-class="bg-slate-900 text-slate-100" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-sm hover:bg-slate-900">
                    <IconTrendingUp class="w-7 h-7 fill-slate-600 group-hover:fill-slate-100" />
                    <p class="self-end text-slate-600 group-hover:text-slate-100">Withdrawal</p>
                </RouterLink>
                <!-- copy experts link -->
                <RouterLink :to="{name: 'home'}" active-class="bg-slate-900 text-slate-100" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-sm hover:bg-slate-900">
                    <IconRefresh class="w-7 h-7 fill-slate-600 group-hover:fill-slate-100" />
                    <p class="self-end text-slate-600 group-hover:text-slate-100">Copy Experts</p>
                </RouterLink>
                <!-- referrals link -->
                <RouterLink :to="{name: 'home'}" active-class="bg-slate-900 text-slate-100" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-sm hover:bg-slate-900">
                    <IconGroup class="w-7 h-7 fill-slate-600 group-hover:fill-slate-100" />
                    <p class="self-end text-slate-600 group-hover:text-slate-100">Referrals</p>
                </RouterLink>
                <!-- settings link -->
                <RouterLink :to="{name: 'home'}" active-class="bg-slate-900 text-slate-100" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-sm hover:bg-slate-900">
                    <IconSetting class="w-7 h-7 fill-slate-600 group-hover:fill-slate-100" />
                    <p class="self-end text-slate-600 group-hover:text-slate-100">Settings</p>
                </RouterLink>

            </div>

        </div>

    </div>
</template>
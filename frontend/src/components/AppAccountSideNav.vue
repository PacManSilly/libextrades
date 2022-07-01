<script setup>
/* eslint-disable */
import { RouterLink, useRoute } from 'vue-router';
import AppLogoVue from './AppLogo.vue';
import IconHome from './icons/IconHome.vue';
import IconUser from './icons/IconUser.vue';
import IconTrendingDown from './icons/IconTrendingDown.vue';
import IconTrendingUp from './icons/IconTrendingUp.vue';
import IconRefresh from './icons/IconRefresh.vue';
import IconGroup from './icons/IconGroup.vue';
import IconSetting from './icons/IconSetting.vue';
import { computed } from 'vue';

// emits
defineEmits(['navClicked'])

// data
const route = useRoute()
</script>

<template>
    <div class="w-full h-screen min-h-full">

        <div class="w-full h-full flex flex-col overflow-y-auto gap-10 items-center bg-slate-800 py-20">

            <!-- start of logo -->
            <div>
                <AppLogoVue />
            </div>

            <div class="flex flex-col gap-2">
                <!-- dashboard link -->
                <RouterLink @click="$emit('navClicked')" :to="{name: 'dashboard'}" :class="route.name == 'dashboard' ? 'bg-slate-900':''" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium transition-all duration-150 rounded-xl hover:bg-slate-900">
                    <IconHome :class="route.name == 'dashboard' ? 'fill-slate-100':'fill-slate-600'" class="w-7 h-7 group-hover:fill-slate-100" />
                    <p :class="route.name == 'dashboard' ? 'text-slate-100':'text-slate-600'" class="self-end group-hover:text-slate-100">Dashboard</p>
                </RouterLink>
                <!-- my profile link -->
                <RouterLink @click="$emit('navClicked')" :to="{name: 'myprofile'}" :class="route.name == 'myprofile' ? 'bg-slate-900':''" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-xl hover:bg-slate-900">
                    <IconUser :class="route.name == 'myprofile' ? 'fill-slate-100':'fill-slate-600'" class="w-7 h-7 group-hover:fill-slate-100" />
                    <p :class="route.name == 'myprofile' ? 'text-slate-100':'text-slate-600'" class="self-end group-hover:text-slate-100">My Profile</p>
                </RouterLink>
                <!-- deposit link -->
                <RouterLink @click="$emit('navClicked')" :to="{name: 'deposit'}" :class="route.name == 'deposit' ? 'bg-slate-900':''" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-xl hover:bg-slate-900">
                    <IconTrendingDown :class="route.name == 'deposit' ? 'fill-slate-100':'fill-slate-600'" class="w-7 h-7 group-hover:fill-slate-100" />
                    <p :class="route.name == 'deposit' ? 'text-slate-100':'text-slate-600'" class="self-end group-hover:text-slate-100">Deposit</p>
                </RouterLink>
                <!-- withdrawal link -->
                <RouterLink @click="$emit('navClicked')" :to="{name: 'withdrawal'}" :class="route.name == 'withdrawal' ? 'bg-slate-900':''" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-xl hover:bg-slate-900">
                    <IconTrendingUp :class="route.name == 'withdrawal' ? 'fill-slate-100':'fill-slate-600'" class="w-7 h-7 group-hover:fill-slate-100" />
                    <p :class="route.name == 'withdrawal' ? 'text-slate-100':'text-slate-600'" class="self-end group-hover:text-slate-100">Withdrawal</p>
                </RouterLink>
                <!-- copy experts link -->
                <RouterLink @click="$emit('navClicked')" :to="{name: 'copyexpert'}" :class="route.name == 'copyexpert' ? 'bg-slate-900':''" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-xl hover:bg-slate-900">
                    <IconRefresh :class="route.name == 'copyexpert' ? 'fill-slate-100':'fill-slate-600'" class="w-7 h-7 group-hover:fill-slate-100" />
                    <p :class="route.name == 'copyexpert' ? 'text-slate-100':'text-slate-600'" class="self-end group-hover:text-slate-100">Copy Experts</p>
                </RouterLink>
                <!-- referrals link -->
                <RouterLink @click="$emit('navClicked')" :to="{name: 'referral'}" :class="route.name == 'referral' ? 'bg-slate-900':''" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-xl hover:bg-slate-900">
                    <IconGroup :class="route.name == 'referral' ? 'fill-slate-100':'fill-slate-600'" class="w-7 h-7 group-hover:fill-slate-100" />
                    <p :class="route.name == 'referral' ? 'text-slate-100':'text-slate-600'" class="self-end group-hover:text-slate-100">Referrals</p>
                </RouterLink>
                <!-- settings link -->
                <RouterLink @click="$emit('navClicked')" :to="{name: 'settings'}" :class="route.name == 'settings' ? 'bg-slate-900':''" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-xl hover:bg-slate-900">
                    <IconSetting :class="route.name == 'settings' ? 'fill-slate-100':'fill-slate-600'" class="w-7 h-7 group-hover:fill-slate-100" />
                    <p :class="route.name == 'settings' ? 'text-slate-100':'text-slate-600'" class="self-end group-hover:text-slate-100">Settings</p>
                </RouterLink>

            </div>

        </div>

    </div>
</template>
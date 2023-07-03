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

// methods
const isRoute = (value) => {
    return route.path.includes(value)
}
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
                <RouterLink @click="$emit('navClicked')" :to="{name: 'dashboard'}" :class="isRoute('dashboard') ? 'bg-gray-900':'bg-transparent'" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium transition-all duration-150 rounded-xl hover:bg-slate-900">
                    <IconHome :class="isRoute('dashboard') ? 'fill-slate-100':'fill-slate-600'" class="w-7 h-7 group-hover:fill-slate-100" />
                    <p :class="isRoute('dashboard') ? 'text-slate-100':'text-slate-600'" class="self-end group-hover:text-slate-100">Dashboard</p>
                </RouterLink>
                <!-- my profile link -->
                <RouterLink @click="$emit('navClicked')" :to="{name: 'myprofile'}" :class="isRoute('myprofile') ? 'bg-gray-900':'bg-transparent'" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-xl hover:bg-slate-900">
                    <IconUser :class="isRoute('myprofile') ? 'fill-slate-100':'fill-slate-600'" class="w-7 h-7 group-hover:fill-slate-100" />
                    <p :class="isRoute('myprofile') ? 'text-slate-100':'text-slate-600'" class="self-end group-hover:text-slate-100">My Profile</p>
                </RouterLink>
                <!-- deposit link -->
                <RouterLink @click="$emit('navClicked')" :to="{name: 'deposit'}" :class="isRoute('deposit') ? 'bg-gray-900':'bg-transparent'" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-xl hover:bg-slate-900">
                    <IconTrendingDown :class="isRoute('deposit') ? 'fill-slate-100':'fill-slate-600'" class="w-7 h-7 group-hover:fill-slate-100" />
                    <p :class="isRoute('deposit') ? 'text-slate-100':'text-slate-600'" class="self-end group-hover:text-slate-100">Invest</p>
                </RouterLink>
                <!-- withdrawal link -->
                <RouterLink @click="$emit('navClicked')" :to="{name: 'withdrawal'}" :class="isRoute('withdrawal') ? 'bg-gray-900':'bg-transparent'" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-xl hover:bg-slate-900">
                    <IconTrendingUp :class="isRoute('withdrawal') ? 'fill-slate-100':'fill-slate-600'" class="w-7 h-7 group-hover:fill-slate-100" />
                    <p :class="isRoute('withdrawal') ? 'text-slate-100':'text-slate-600'" class="self-end group-hover:text-slate-100">Withdrawal</p>
                </RouterLink>
                <!-- copy experts link -->
                <RouterLink @click="$emit('navClicked')" :to="{name: 'copyexpert'}" :class="isRoute('copyexpert') ? 'bg-gray-900':'bg-transparent'" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-xl hover:bg-slate-900">
                    <IconRefresh :class="isRoute('copyexpert') ? 'fill-slate-100':'fill-slate-600'" class="w-7 h-7 group-hover:fill-slate-100" />
                    <p :class="isRoute('copyexpert') ? 'text-slate-100':'text-slate-600'" class="self-end group-hover:text-slate-100">Copy Experts</p>
                </RouterLink>
                <!-- referrals link -->
                <RouterLink @click="$emit('navClicked')" :to="{name: 'referral'}" :class="isRoute('referral') ? 'bg-gray-900':'bg-transparent'" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-xl hover:bg-slate-900">
                    <IconGroup :class="isRoute('referral') ? 'fill-slate-100':'fill-slate-600'" class="w-7 h-7 group-hover:fill-slate-100" />
                    <p :class="isRoute('referral') ? 'text-slate-100':'text-slate-600'" class="self-end group-hover:text-slate-100">Referrals</p>
                </RouterLink>
                <!-- settings link -->
                <RouterLink @click="$emit('navClicked')" :to="{name: 'settings'}" :class="isRoute('settings') ? 'bg-gray-900':'bg-transparent'" class="group flex items-center justify-start gap-2 px-4 py-2 text-base font-medium bg-transparent transition-all duration-150 rounded-xl hover:bg-slate-900">
                    <IconSetting :class="isRoute('settings') ? 'fill-slate-100':'fill-slate-600'" class="w-7 h-7 group-hover:fill-slate-100" />
                    <p :class="isRoute('settings') ? 'text-slate-100':'text-slate-600'" class="self-end group-hover:text-slate-100">Settings</p>
                </RouterLink>

            </div>

        </div>

    </div>
</template>
<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { RouterView } from 'vue-router';
import AppAccountSideNavVue from '../components/AppAccountSideNav.vue';
import IconHamburger from '../components/icons/IconHamburger.vue';
import AppUserAvatar from '../components/AppUserAvatar.vue';
import { computed } from 'vue';
import { useUserStore } from '../stores/user';
import IconUserClose from '../components/icons/IconUserClose.vue';
import IconSetting from '../components/icons/IconSetting.vue';
import IconHome from '../components/icons/IconHome.vue';

// refs
const menu = ref(false)

// stores
const store = useUserStore()

// computed
const isAuthenticated = computed(() => {
  if (JSON.parse(localStorage.getItem('libex_token'))) return true
  else return false
})
</script>

<template>
    <div class="w-full h-full min-h-screen bg-slate-900">

        <div class="w-full h-full flex relative">

            <!-- start of top nav-->
            <div class="absolute top-0 w-full lg:w-auto z-10 bg-slate-900 lg:bg-transparent lg:right-10">
                <div class="w-full mx-auto py-6 px-4 flex justify-between items-center">
                    <button @click.prevent="menu = true" class="block lg:hidden" type="button">
                        <IconHamburger class="w-10 h-10 fill-slate-600 hover:fill-slate-100" />
                    </button>
                    <div class="flex items-center gap-x-3">
                        <RouterLink :to="{name: 'dashboard'}">
                            <IconHome class="w-7 h-7 text-slate-400" />
                        </RouterLink>

                        <AppUserAvatar />

                        <RouterLink :to="{name: 'settings'}">
                            <IconSetting class="w-7 h-7 text-slate-400" />
                        </RouterLink>
                    </div>
                </div>
            </div>


            <!-- mobile version toggable -->
            <div class="fixed w-9/12 z-10 md:w-5/12 lg:w-2/12">
                <div
                    :class="menu ? 'translate-x-0':'-translate-x-full'"
                    class="flex w-full absolute top-0 bg-slate-800 shadow-2xl transition transform duration-150 lg:hidden">
                    <AppAccountSideNavVue @nav-clicked="menu = false"/>
                </div>
                <!-- large screen version -->
                <div class="hidden bg-slate-800 transition transform duration-150 lg:flex">
                    <AppAccountSideNavVue @nav-clicked="menu = false" />
                </div>
            </div>

            <!-- start of account main -->
            <div
                @click="menu = false"
                class="fixed right-0 w-full h-full overflow-y-auto py-20 px-5 lg:px-10 lg:w-10/12">
                <RouterView />
            </div>
            <!-- start of account main -->


        </div>


        <!-- is suspended effect -->
        <div v-if="store.userData.data.is_suspended" class="fixed top-0 left-0 right-0 w-full h-full bg-white/10 backdrop-blur-md z-30">

            <div class="w-10/12 h-full flex flex-col justify-center mx-auto md:w-7/12 lg:w-5/12">

                <div class="flex flex-col">
                    <IconUserClose class="w-32 h-32 text-slate-400 md:h-40 md:w-40" />
                    <p class="text-3xl font-black text-slate-400">Account Suspended</p>
                </div>

                <div class="bg-black w-full flex flex-col gap-y-3 py-10 px-10 mt-5">
                    <p class="text-xl text-slate-400 font-black md:text-2xl">This account has been suspended.</p>
                    <span class="flex items-center gap-x-2 text-white">
                        <p>Please contact</p>
                        <a href="mailto:support@libextrades.com" class="text-blue-400 font-black hover:text-blue-500">support</a>
                    </span>

                    <span class="mt-10">
                        <button type="button" @click="store.userSignOut.modal = true" class="text-blue-400">Sign out</button>
                    </span>
                </div>

            </div>
        </div>
        <!-- is suspended effect -->

    </div>
</template>
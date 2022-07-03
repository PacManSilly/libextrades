<script setup>
/* eslint-disable */
import { ref, computed } from 'vue';
import IconSetting from './icons/IconSetting.vue';
import IconCloseBig from './icons/IconCloseBig.vue'
import AppAccountSettingProfile from './AppAccountSettingProfile.vue';
import AppAccountSettingEmail from './AppAccountSettingEmail.vue';
import AppAccountSettingPassword from './AppAccountSettingPassword.vue';
import AppAccountSettingAddress from './AppAccountSettingAddress.vue';
import AppAccountSettingIdentity from './AppAccountSettingIdentity.vue';
import { useUserStore } from '../stores/user';

// stores
const store = useUserStore()

// data
const tabId = ref()
const tabs = [
    {id: 1, name: 'Profile'},
    {id: 2, name: 'Email'},
    {id: 3, name: 'Password'},
    {id: 4, name: 'Address'},
    {id: 5, name: 'Verify Identity'},
]

// co,puted
const activeTab = computed(() => {
    return tabs.find((tab) => tab.id == tabId.value)
})

// methods
const edit = (id) => {
    store.profileUpdate.modal = true
    tabId.value = id
}
</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="w-full h-full flex flex-col">

            <div class="flex flex-col gap-2 pb-5 mt-10 mb-10 border-b border-slate-700 lg:mt-0">
                <h1 class="text-white text-4xl font-black">Settings</h1>
                <span class="text-slate-600 font-normal tracking-wide">Update your account settings</span>
            </div>

            <div class="w-full flex flex-col gap-10 mt-10 items-center justify-between pb-10 md:gap-20 md:justify-center md:flex-row">

                <div class="w-full md:w-1/2 lg:w-3/12">
                    <div class="w-full bg-slate-800 p-4 flex flex-col items-start gap-2 rounded-md">
                        <button @click.prevent="edit(tab.id)" v-for="tab in tabs" :key="tab.id" class="w-full text-left text-slate-600 text-base font-medium p-2 bg-transparent rounded transition-all duration-150 hover:text-white hover:bg-slate-900 md:text-lg">{{tab.name}}</button>
                    </div>
                </div>

                <div class="w-full h-full flex items-center justify-start">
                    <div class="w-full h-60 p-4 flex flex-col items-center justify-center border-2 border-dashed border-slate-700 rounded-lg bg-slate-800 md:h-72 lg:p-0 lg:w-1/2">
                        <IconSetting class="w-20 h-20 fill-slate-700" />
                        <p class="text-center text-slate-700 font-medium text-sm md:text-base">Select the data you would like to update</p>
                    </div>
                </div>

            </div>

        </div>


        <!-- withdrawal modal -->
        <teleport to="body">
            <transition
                enter-from-class="scale-0 opacity-0"
                enter-active-class="transition-all duration-150"
                leave-to-class="scale-0 opacity-0"
                leave-active-class="transition-all duration-150">
                <div v-if="store.profileUpdate.modal" class="w-full absolute top-0 z-30 h-screen min-h-[40rem] bg-slate-900/90 backdrop-blur-lg">

                    <div class="w-full h-full relative flex items-center justify-center">
                        
                        <!-- close button -->
                        <button @click.prevent="store.profileUpdate.modal = false" type="button" class="absolute group top-5 left-5 p-2 rounded transition-all duration-150 hover:bg-slate-800">
                            <IconCloseBig class="w-10 h-10 fill-slate-400 group-hover:fill-slate-200" />
                        </button>

                        <div class="w-10/12 flex flex-col gap-10 items-center lg:w-1/2">
                            <AppAccountSettingProfile v-if="activeTab.name == 'Profile'" />
                            <AppAccountSettingEmail v-if="activeTab.name == 'Email'" />
                            <AppAccountSettingPassword v-if="activeTab.name == 'Password'" />
                            <AppAccountSettingAddress v-if="activeTab.name == 'Address'" />
                            <AppAccountSettingIdentity v-if="activeTab.name == 'Verify Identity'" />
                        </div>
                        
                    </div>
                </div>
            </transition>
        </teleport>

    </div>
</template>
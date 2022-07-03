<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { useUserStore } from '../stores/user';
import AppButton from './AppButton.vue';
import IconFileImage from './icons/IconFileImage.vue';

// stores
const store = useUserStore()

// data
const frontView = ref(null)
const backView = ref(null)

// methods
const updateIdentity = () => {
    const formData = new FormData()

    if (frontView.value.files[0]) formData.append('kyc_front_view', frontView.value.files[0], frontView.value.files[0].name)
    if (backView.value.files[0]) formData.append('kyc_back_view', backView.value.files[0], backView.value.files[0].name)

    store.updateMe(formData)
}
</script>

<template>
    <div class="w-full h-full min-h-full mx-auto">

        <form @submit.prevent="updateIdentity" class="w-full h-full flex flex-col gap-5 md:w-10/12">

            <div class="mb-10 flex flex-col gap-2">
                <h1 class="text-white font-black text-2xl md:text-4xl">Proof of Identity</h1>
                <span class="text-slate-500 text-sm">
                    Due to government requirements, you need to go through a KYC process to verify your identity.
                    Please provide us a valid government issued identification card, for verification.
                </span>
            </div>

            <!-- start of handle errors  -->
            <transition
                enter-from-class="-translate-y-5 opacity-0"
                enter-active-class="transitiona-ll duration-150"
                leave-to-class="-translate-y-5 opacity-0"
                leave-active-class="transitiona-ll duration-150">
                <ul v-if="error || store.profileUpdate.error || store.profileUpdate.success" class="flex flex-col text-xs list-inside md:text-sm">
                    <li v-if="error || store.profileUpdate.error" class="text-red-600">{{store.profileUpdate.error || error}}</li>
                    <li v-else-if="store.profileUpdate.success" class="text-green-600">{{store.profileUpdate.success}}</li>
                </ul>
            </transition>

            <div class="w-full flex flex-col gap-5">
                <!-- front view -->
                <div class="flex flex-col gap-2">
                    <label for="front" class="text-slate-400 text-xs font-normal md:text-sm">Front View</label>
                    <div class="w-full h-40 flex flex-col gap-2 items-center justify-center rounded-lg border-2 border-dashed border-slate-700 bg-slate-800">
                        <IconFileImage class="w-10 h-10 fill-slate-700" />
                        <input type="file" ref="frontView" required name="front" id="front" class="transition-all duration-150 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-xs file:font-semibold file:bg-slate-100 file:text-blue-600 hover:file:bg-slate-100 hover:text-slate-100 md:file:text-sm">
                    </div>
                </div>

                <!-- back view -->
                <div class="flex flex-col gap-2">
                    <label for="front" class="text-slate-400 text-xs font-normal md:text-sm">Back View</label>
                    <div class="w-full h-40 flex flex-col gap-2 items-center justify-center rounded-lg border-2 border-dashed border-slate-700 bg-slate-800">
                        <IconFileImage class="w-10 h-10 fill-slate-700" />
                        <input type="file" ref="backView" required name="front" id="front" class="transition-all duration-150 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-xs file:font-semibold file:bg-slate-100 file:text-blue-600 hover:file:bg-slate-100 hover:text-slate-100 md:file:text-sm">
                    </div>
                </div>
            </div>

            <div class="w-full flex md:justify-end">
                <AppButton name="Save" class="w-full md:w-1/4" :loading="store.profileUpdate.loading" />
            </div>

        </form>

    </div>
</template>
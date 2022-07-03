<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { useUserStore } from '../stores/user';
import AppInputField from './AppInputField.vue';
import AppButton from './AppButton.vue';

// stores
const store = useUserStore()

// data
const country = ref(null)
const state = ref(null)
const city = ref(null)

// methods
const updateAddress = () => {
    const formData = new FormData()

    if (country.value) formData.append('country', country.value)
    if (country.value) formData.append('state', state.value)
    if (country.value) formData.append('city', city.value)

    store.updateMe(formData)
}
</script>

<template>
    <div class="w-full h-full min-h-full mx-auto">

        <form @submit.prevent="updateAddress" class="w-full h-full flex flex-col gap-5 md:w-10/12">

            <div class="text-center mb-10">
                <h1 class="text-white font-black text-2xl md:text-4xl">Update Your Address</h1>
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

            <div class="w-full">
                <AppInputField v-model="country" label="Country" placeholder="Enter country..." />
            </div>

            <div class="w-full grid gap-3 grid-cols-1 md:grid-cols-2">
                <AppInputField v-model="state" label="State" placeholder="Enter state..." />
                <AppInputField v-model="city" label="City" placeholder="Enter city..." />
            </div>

            <div class="w-full flex md:justify-end">
                <AppButton name="Update" class="w-full md:w-1/4" :loading="store.profileUpdate.loading" />
            </div>

        </form>

    </div>
</template>
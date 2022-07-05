<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { useUserStore } from '../stores/user';
import btclogo from '../assets/images/btc.png';
import AppInputField from './AppInputField.vue';
import AppButton from './AppButton.vue';

// store
const store = useUserStore()

// data
const mugshot = ref(null)
const fname = ref(null)
const lname = ref(null)
const oname = ref(null)
const dob = ref(null)
const phone = ref(null)

// methods
const updateProfile = () => {
    const formData = new FormData()
    if (fname.value) formData.append('first_name', fname.value)
    if (lname.value) formData.append('last_name', lname.value)
    if (oname.value) formData.append('other_name', oname.value)
    if (dob.value) formData.append('dob', dob.value)
    if (phone.value) formData.append('phone', phone.value)
    if (mugshot.value.files[0]) formData.append('mugshot', mugshot.value.files[0], mugshot.value.files[0].name)

    store.updateMe(formData)
}
</script>

<template>
    <div class="w-full h-full min-h-full mx-auto">

        <form @submit.prevent="updateProfile" class="w-full h-full flex flex-col gap-5 md:w-10/12">

            <div class="text-center mb-10">
                <h1 class="text-white font-black text-2xl md:text-4xl">Update Your Profile</h1>
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

            <div class="flex flex-col gap-2 md:flex-row">
                <div class="flex items-center justify-center h-16 w-16 overflow-hidden bg-slate-100 rounded-full">
                    <img v-if="store.userData.data.mugshot" :src="store.userData.data.mugshot" class="h-full w-full object-cover object-center">
                    <p v-else class="font-black text-2xl text-slate-900">{{store.userData.data.first_name[0]}}</p>
                </div>
                <input type="file" ref="mugshot" name="mugshot" id="mugshot" class="self-end text-blue-600 transition-all duration-150 file:cursor-pointer file:mr-4 file:py-2 file:px-2 file:rounded-full file:border-0 file:text-xs file:font-semibold file:bg-slate-100 file:text-blue-600 hover:file:bg-slate-100">
            </div>

            <div class="w-full grid gap-3 grid-cols-1 mt-5 md:grid-cols-2">
                <AppInputField :required="false" v-model="fname" label="First Name" />
                <AppInputField :required="false" v-model="lname" label="Last Name" />
            </div>

            <div class="w-full grid gap-3 grid-cols-1 md:grid-cols-2">
                <AppInputField :required="false" v-model="oname" label="Other Name" />
                <AppInputField :required="false" v-model="dob" label="Date of Birth" type="date" />
            </div>

            <div>
                <AppInputField :required="false" v-model="phone" label="Phone Number" placeholder="+1 (555) 123-4567" />
            </div>

            <div class="w-full flex md:justify-end">
                <AppButton name="Update" class="w-full md:w-1/4" :loading="store.profileUpdate.loading" />
            </div>

        </form>

    </div>
</template>
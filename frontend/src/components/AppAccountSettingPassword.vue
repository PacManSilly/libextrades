<script setup>
/* eslint-disable */
import AppButton from './AppButton.vue';
import AppPasswordField from './AppPasswordField.vue';

</script>

<template>
    <div class="w-full h-full min-h-full mx-auto">

        <div class="w-full h-full flex flex-col gap-5 md:w-10/12">

            <div class="text-center mb-10">
                <h1 class="text-white font-black text-2xl md:text-4xl">Change Your Account Password</h1>
            </div>
            
            <div class="w-full flex flex-col gap-3">
                <AppPasswordField label="New Password" />
                <AppPasswordField label="Confirm New Password" />
            </div>

            <div class="w-full flex md:justify-end">
                <AppButton name="Save" class="w-full md:w-1/4" />
            </div>

        </div>

    </div>
</template>
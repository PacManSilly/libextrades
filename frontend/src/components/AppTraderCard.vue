<script setup>
/* eslint-disable */
import IconCheckBold from './icons/IconCheckBold.vue';

// props
const props = defineProps({
    id: {type: String},
    name: {type: String},
    mugshot: {type: String, default: false},
    rate: {type: String, default: "90%"},
    share: {type: String, default: "20%"},
    active: {type: Boolean, default: false},
})

// emits
defineEmits(['traderClicked'])
</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="relative w-full min-w-[10rem] flex gap-3 bg-slate-800 p-3 rounded-md shadow-lg">

            <div class="w-10 h-10 flex shrink-0 items-center justify-center bg-slate-900 shadow-lg rounded-full overflow-hidden">
                <img v-if="props.mugshot" :src="props.mugshot" alt="Picture" class="w-full h-full object-cover object-center">
                <p v-else class="font-black text-2xl text-white">{{props.name[0]}}</p>
            </div>
            <div class="flex flex-col items-start truncate">
                <button type="button" @click.prevent="$emit('traderClicked', props.id)" class="max-w-[10rem] text-blue-600 text-base font-medium text-left truncate md:max-w-[6rem] lg:max-w-[5rem] xl:max-w-[14rem]">{{props.name}}</button>
                <span class="text-sm font-normal text-slate-500">Win Rate: {{props.rate}}</span>
                <span class="text-sm font-normal text-slate-500">Profit Share: {{props.share}}</span>
            </div>

            <div v-if="props.active" class="h-5 w-5 rounded-full overflow-hidden bg-green-600 flex items-center justify-center absolute top-2 right-3">
                <IconCheckBold class="w-3 h-3 fill-white" />
            </div>
        </div>
    
    </div>
</template>
<script setup>
/* eslint-disable */
import IconLoadingVue from "./icons/IconLoading.vue"


// props
const props = defineProps({
    name: {type: String, default: "Submit"},
    loading: {type: Boolean, default: false},
    bgColor: {type: String, default: 'blue'},
    textColor: {type: String, default: 'white'}
})
</script>

<template>
  <div class="w-full">
    <button
        type="submit"
        :disabled="loading"
        :class="[props.bgColor == 'white' ? 'bg-white hover:bg-slate-200':'bg-blue-500 hover:bg-blue-600',
        props.textColor == 'white' ? 'text-white':'text-slate-900']"
        class="w-full p-2 text-center text-sm rounded transition-all duration-150
        disabled:bg-slate-800 disabled:cursor-wait">
        <div v-if="props.loading" class="w-full flex items-center justify-center">
            <IconLoadingVue class="animate-spin" />
        </div>
        <p v-else class="font-medium text-sm md:text-base">{{props.name}}</p>
    </button>
  </div>
</template>
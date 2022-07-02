<script setup>
/* eslint-disable */
// props
const props = defineProps({
    id: {type: Number},
    method: {type: String, default: "String"},
    amount: {type: String, default: "String"},
    created: {type: String, default: "String"},
    status: {type: String, default: "Pending"},
})

// emits
defineEmits(['payNow'])

const toDate = new Date(props.created).toDateString()
</script>

<template>
    <div class="w-full h-full">

        <div class="w-full bg-slate-900 px-4 py-2 flex flex-col gap-5 divide-y divide-slate-700 items-start rounded-md md:flex-row md:divide-y-0 md:justify-between">
            <div class="w-full flex flex-col gap-2 p-2 md:w-auto md:p-0">
                <span class="text-slate-200 font-normal text-base">Method</span>
                <span class="text-slate-600 font-medium text-sm">{{method}}</span>
            </div>

            <div class="w-full flex flex-col gap-2 p-2 md:w-auto md:p-0">
                <span class="text-slate-200 font-normal text-base">Date Created</span>
                <span class="text-slate-600 font-medium text-sm">{{toDate}}</span>
            </div>

            <div class="w-full flex flex-col gap-2 p-2 md:w-auto md:p-0">
                <span class="text-slate-200 font-normal text-base">Status</span>
                <span class="text-white font-medium text-xs flex gap-2">
                    <span :class="props.status == 'Active' ? 'bg-green-600':'bg-yellow-600'" class="text-white p-2 rounded-full">{{props.status}}</span>
                </span>
            </div>
        </div>
        
    </div>
</template>
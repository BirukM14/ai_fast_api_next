import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
    const { input } = await req.json();
    return NextResponse.json({ message: `Received: ${input}` });
}

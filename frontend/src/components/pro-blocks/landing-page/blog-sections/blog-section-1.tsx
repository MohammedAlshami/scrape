"use client";

import { AspectRatio } from "@/components/ui/aspect-ratio";
import Image from "next/image";
import Link from "next/link";
import { Tagline } from "@/components/pro-blocks/landing-page/tagline";

interface BlogPost {
  id: number;
  title: string;
  description: string;
  date: string;
  category: string;
  image: string;
}

export function BlogSection1({ posts }: { posts: BlogPost[] }) {
  return (
    <section
      className="bg-background section-padding-y"
      aria-labelledby="blog-section-heading"
    >
      <div className="container-padding-x mx-auto max-w-7xl gap-10 md:gap-12">
        <div className="flex flex-col items-center gap-10 md:gap-12">
          <div className="section-title-gap-lg mx-auto flex max-w-xl flex-col items-center text-center">
            <Tagline>Blog Section</Tagline>
            <h1 id="blog-section-heading" className="heading-lg">
              Learn what's new
            </h1>
            <p className="text-muted-foreground text-lg/8 text-pretty">
              Add a concise value statement that captures your reader's interest
              and previews your content value.
            </p>
          </div>
          <div
            className="grid grid-cols-1 gap-8 md:grid-cols-2 md:gap-4 lg:grid-cols-4"
            role="list"
          >
            {posts.map((post) => (
              <Link href="#" key={post.id} className="group block">
                <div className="flex flex-col gap-4 rounded-xl transition-all duration-200">
                  <AspectRatio
                    ratio={4 / 3}
                    className="overflow-hidden rounded-xl"
                  >
                    <Image
                      src={post.image}
                      alt={`${post.title} thumbnail`}
                      fill
                      className="h-full w-full object-cover transition-transform duration-200 group-hover:scale-105"
                    />
                  </AspectRatio>
                  <div className="flex flex-col gap-3">
                    <div className="flex items-center gap-2 text-left">
                      <span className="text-muted-foreground text-sm">
                        {post.date}
                      </span>
                      <span className="text-muted-foreground text-sm">·</span>
                      <span className="text-muted-foreground text-sm">
                        {post.category}
                      </span>
                    </div>
                    <h3 className="text-base font-semibold tracking-tight group-hover:underline">
                      {post.title}
                    </h3>
                    <p className="text-muted-foreground text-sm">
                      {post.description}
                    </p>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
